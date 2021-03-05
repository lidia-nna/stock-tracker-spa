<template>
  <v-row justify="center" align-content="center">
    <v-col cols='10' sm="8" lg="6" xl="4" align="center"> 
      <v-img src="../assets/logo.png" width="50%" alt=""></v-img>
      <register-form></register-form>
    </v-col>
  </v-row> 
</template>

<script>
import RegisterForm from '../components/RegisterForm';

export default {
  components: { RegisterForm },
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