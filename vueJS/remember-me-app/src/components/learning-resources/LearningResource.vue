<template>
  <div class="card mb-5">
    <div class="card-header">
      <div class="d-flex flex-row justify-content-between">
        <div class="display-6">{{ title }}</div>
        <div class="mt-1">
          <button class="btn btn-outline-danger" @click="deleteResource(id)">Delete</button>
        </div>
      </div>
    </div>
    <div class="card-body">
      <p>{{ description }}</p>
      <nav>
        <a :href="link">View Source</a>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  props: ["id", "title", "description", "link"],
  inject: ["deleteResource"],
};
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>
