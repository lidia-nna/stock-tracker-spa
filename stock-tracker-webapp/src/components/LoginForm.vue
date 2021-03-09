<template>
    <v-form
    ref="form"
    v-model="valid"
    lazy-validation
    @submit.prevent="onSubmit"
    class="rounded"
    >
    <v-card-text class="pink--text" v-if="error">{{authStatus}}</v-card-text>
    <v-card
    class="bccolor elevation-10 mb-2 pt-5"
    >
      <br>
      <v-row class="d-flex justify-center" >
        <v-col cols="10" sm="8" md="6" lg="8" xl="8" align-content='center'>
          <p class="text-center text-h5">
            Sign in
          </p>
          <v-text-field
          v-model="username"
          :counter="10"
          :rules="nameRules"
          label="Username"
          required
        ></v-text-field>

        <!-- <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field> -->

        <v-text-field
          v-model="password"
          :rules="passwordRules"
          label="Password"
          :type="show ? 'text' : 'password'"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="show = !show"
          required
          counter
        ></v-text-field>

        </v-col>
      </v-row>
   
    <v-row class="d-flex justify-center">
    <v-btn
      :disabled="!valid"
      color="#00bcd4"
      class="mr-4"
      type="submit"
    >
      Sumbit
    </v-btn>

    <v-btn
      color="#00bcd4"
      @click="reset"
    >
      Clear
    </v-btn>
    </v-row><br><br>
    </v-card>
  </v-form>
</template>

<script>
import {mapActions, mapState, mapMutations} from 'vuex'
export default {
    name: 'LoginForm',
    data: () => ({
      valid: true,
      show: false,
      username: 'demo',
      error: false,
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      // email: '',
      // emailRules: [
      //   v => !!v || 'E-mail is required',
      //   v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      // ],
      password:'11111111',
      passwordRules: [
          v => !! v || 'Password is required',
          v => v.length >= 8 || 'Password must be at least 8 characters'
      ]
    }),
    computed: {
      ...mapState({
        authStatus: (state) => state.auth.authStatus
      })
    },

    methods: {
      ...mapMutations(['setStatus']),
      ...mapActions(['login', 'register']),
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
        this.setStatus("")
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
      async onSubmit () {
        this.validate()
        let form = new FormData();
        form.append('username', this.username)
        form.append('password', this.password)
        try {
          await this.login(form)
        } catch(error) {
          console.error('Login',error)
          this.error=true
        }
        // this.reset()
        // this.$router.push("/user");
      }
    },
}
</script>
<style scoped>
[v-cloak] {
  display: none;
}
.bccolor {
  background-color: #272727;
}

</style>