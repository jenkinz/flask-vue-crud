<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PingComponent',
  setup() {},
  data() {
    return {
      msg: 'Hello!',
    };
  },
});
</script>

<template>
  <div>
    <router-link to="/">Home</router-link>
    <p>{{ msg }}</p>
  </div>
</template>
