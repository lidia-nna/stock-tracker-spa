<template>
    <v-form
    ref="form"
    v-model="valid"
    lazy-validation
    @submit.prevent="onSubmit"
  >

    <v-card>
      <br>
      <v-row class="d-flex justify-center" >
        <v-col cols="12" sm="6" md="6" align-content='center'>
          <p class="text-center text-h5">
            Sign up
          </p>
          <v-text-field
          v-model="username"
          :counter="10"
          :rules="nameRules"
          label="Username"
        ></v-text-field>

        <v-text-field
          v-model.lazy="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :type="show ? 'text' : 'password'"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="show = !show"
          :rules="passwordRules"
          counter
          label="Password"
          required
        ></v-text-field>
         <v-text-field
          v-model="confpassword"
          :rules="confpasswordRules"
          label="Confirm password"
          required
          counter
          :type="show ? 'text' : 'password'"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="show = !show"
        ></v-text-field>
        
        <v-checkbox
          v-model="checkbox"
          :rules="[v => !!v || 'You must agree to continue!']"
          label="Do you agree?"
          required
        ></v-checkbox>
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
import {mapActions} from 'vuex'
export default {
    name: 'RegisterForm',
    data: () => ({
      valid: true,
      show:false,
      username: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      password:'',
      passwordRules: [
          v => !! v || 'Password is required',
          v => v.length >= 8 || 'Password must be at least 8 characters'
      ],
      confpassword:'',
      checkbox: false,
      // regForm: {
      //   username: '',
      //   email: '',
      //   password: ''
      // }
    }),
    computed: {
      confpasswordRules() {
        return [this.confpassword == this.password || 'Password must match']
      },
      regForm (){
        let form = new FormData();
        form.append('username', this.username)
        form.append('email', this.email)
        form.append('password', this.password)
        return form
      }
    },
    
    methods: {
      ...mapActions(['login', 'register']),
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
      async onSubmit () {
        this.validate()
        await this.register(this.regForm)
        this.reset()
      }
    },
}
</script>