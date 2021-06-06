<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
    </v-app-bar>

    <v-main>
      <todoTask/>
    </v-main>
  </v-app>
</template>

<script>
import todoTask from './components/todo/todoTask';

export default {
  name: 'App',

  components: {
    todoTask,
  },

  data: () => ({
    //
  }),
};
</script>
