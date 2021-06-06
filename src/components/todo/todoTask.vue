<template>
  <div>
    <br /><br /><br /><br />
    <v-container>
    <v-row>
      <h1>My Todos</h1>
    </v-row>
    <br /><br /><br /><br />
      <v-row>
        <v-col cols="6">
          <v-text-field 
            label="Create a new todo..."
            @keyup.enter="createToDo()"
            v-model="newTodo"
            outlined
            dense
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6">
            <todoList 
              v-for="(todo, i) in todoList"
              :key=i
              :content="todo.content"
              :val="todo.val"
              @on-toggle="toggleTodo(todo)"
              @on-delete="deleteTodo(todo.id)"
              @on-edit="editTodo(todo.id, $event)"
            />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import todoList from './todoList';

export default {
  name: 'todoTask',
  components: {
    todoList,
  },
  data: () => ({
    todoList: [{
      content: null,
      val: false
    }],
    newTodo: null,
    headers: [
        {
          text: 'Name',
          align: 'start',
          sortable: false,
          value: 'content',
        },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
  }),
  created() {
    this.getTodoList();
  },
  methods: {
    getTodoList() {
      this.axios({
        methods: 'get',
        url:'/task',
        auth: {
          username: 'malathi',
          password: 'malathi@98',
        },
      }).then((response) => {
        if (response) {
          this.todoList = response.data;
        }
      })
    },
    createToDo() {
      var responseBody = {
        'content': this.newTodo
      }
      this.axios({
        method: 'post',
        url:'/task/',
        auth: {
          username: 'malathi',
          password: 'malathi@98',
        },
        data: responseBody,
      }).then((response) => {
          if (response) {
          this.getTodoList();
        }
      })
    },
    toggleTodo(todo) {
      todo.val = !todo.val;
    },
    deleteTodo(id) {
      this.axios({
        method: 'delete',
        url:'/task/'+ id + '/',
        auth: {
          username: 'malathi',
          password: 'malathi@98',
        }
      }).then((response) => {
        if (response) {
          this.getTodoList();
        }
      })
    },
    editTodo(id, newTodoContent) {
      console.log("edit", newTodoContent)
      this.axios({
        method: 'put',
        url:'/task/'+id+'/',
        auth: {
          username: 'malathi',
          password: 'malathi@98',
        },
        data: {
          content : newTodoContent
        },
      }).then((response) => {
        if (response) {
          this.getTodoList();
        }
      })
    },
  }
}
</script>
