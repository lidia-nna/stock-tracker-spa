<template>
  <v-row class="gradient" justify="center" align="start">
    <v-col cols='8' sm="7" md="5" lg="4" xl="4" align="center" v-cloak> 
      <v-img src="../assets/logo.png" width="47%" alt=""></v-img>
      <router-view></router-view>
    </v-col>
  </v-row> 
</template>

<script>
// import RegisterForm from '../components/RegisterForm';

export default {
//   components: { RegisterForm },
    name: 'Register',
    data: () => ({
      valid: true,
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      passwordRules: [
          v => !! v || 'Password is required',
          v => v.length >= 8 || 'Password must be at least 8 characters'
      ],
      checkbox: false,
      form: {
        username: '',
        email: '',
        password: ''
      }
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },
  
}
</script>
<style scoped>
[v-cloak] {
  display: none;
}
.gradient {
  min-height: 100%;
  background: linear-gradient(125deg,#1e1e1e 10%,#00bcd4 160%);
  margin:0
}

</style>