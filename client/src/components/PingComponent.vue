<script>
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'PingComponent',
  setup() {},
  data() {
    return {
      msg: 'Default',
    };
  },
  created() {
    this.getMessage();
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
});
</script>

<template>
  <div>
    <router-link to="/">Home</router-link>
    <p>{{ msg }}</p>
  </div>
</template>
