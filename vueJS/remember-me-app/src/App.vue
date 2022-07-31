<template>
  <the-header title="My Learning"></the-header>
  <the-resources></the-resources>
</template>

<script>
// local components
import TheHeader from "./components/layouts/TheHeader.vue";
import TheResources from "./components/learning-resources/TheResources.vue";

export default {
  components: {
    TheHeader,
    TheResources,
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}

html {
  font-family: sans-serif;
}

body {
  margin: 0;
}
</style>
