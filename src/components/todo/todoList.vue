<template>
  <v-flex>
    <li class="d-flex align-items-center list-group-item">
    <button
        class="btn border-0 flex-grow-1 text-left shadow-none"  
        @click="$emit('on-toggle')"
        v-if="!isEditing"
        :class="{val}">
        <span>{{ content }}</span>
      </button>
      <form v-else class="flex-grow-1">
        <input
          type="text"
          class="form-control"
          v-model="newTodoContent"
          @blur="editingCompleted()"
          ref="newTodo"
        />
      </form>
      <button class="btn btn-outline-primary border-0">
      <v-icon color="blue" medium class="mr-2" @click="startEditing()">mdi-pencil</v-icon>
      </button>
      <button class="btn btn-outline-primary border-0 ml-2">
        <v-icon color="red" medium class="mr-2" @click="$emit('on-delete')"> mdi-delete</v-icon>
      </button>
    </li>
  </v-flex>
</template>

<script>

export default {
  name: 'todoList',
  props: ['content', "val"],
  data: () => ({
    newTodoContent: null,
    isEditing: false,
    todoList: null,
    headers: [
      { text: 'Name', value: 'content' },
      { text: 'Actions', value: 'actions', sortable: false },
    ]
  }),
  methods: {
    startEditing() {
      if (this.isEditing) {
        this.editingCompleted();
      } else {
        this.newTodoContent = this.content;
        this.isEditing = true;
        this.$nextTick(() => this.$refs.newTodo.focus());
      }
    },
    editingCompleted(){
      this.isEditing = false;
      this.$emit("on-edit", this.newTodoContent);
    },
  }
}
</script> !important;

<style scoped>
.val{
  text-decoration: line-through;
}
.d-flex{
  display: flex !important
}
.ml-2 .mx-2{
  margin-left: .5rem!important;
}
.btn-outline-primary{
    color: #007bff;
    border-color: #007bff;
}
.list-group {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-direction: column;
    flex-direction: column;
    padding-left: 0;
    margin-bottom: 0;
}
.list-group-item{
    position: relative;
    display: block;
    padding: .75rem 1.25rem;
    background-color: #fff;
    border: 1px solid rgba(0,0,0,.125);
}
.text-left {
  text-align: left
}
.shadow-none{
  box-shadow: none !important;
}
.flew-grow-1{
  flex-grow: 1!important;
}
.border-0 {
  border: 0!important;
}
.btn {
    display: inline-block;
    font-weight: 400;
    color: #212529;
    text-align: center;
    vertical-align: middle;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-color: transparent;
    border: 1px solid transparent;
    padding: .375rem .75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: .25rem;
    transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}
</style>

