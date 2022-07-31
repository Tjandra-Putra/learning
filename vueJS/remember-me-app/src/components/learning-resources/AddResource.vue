<template>
  <base-dialogue v-if="inputIsInvalid" title="Invalid input" @close="confirmError">
    <template #default>
      <p>Unfortunately, at least one input value is invalid.</p>
      <p>Please check the fields again.</p>
    </template>
    <template #actions>
      <button class="btn btn-secondary" @click="confirmError">Okay</button>
    </template>
  </base-dialogue>
  <div class="container shadow p-4 rounded-3">
    <div class="display-6">Add Resource</div>
    <form @submit.prevent="submitData">
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input type="text" class="form-control" id="title" name="title" ref="titleInput" />
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea class="form-control" id="description" name="description" rows="3" ref="descInput"></textarea>
      </div>
      <div class="mb-3">
        <label for="link" class="form-label">Link</label>
        <input type="url" class="form-control" id="link" name="link" ref="linkInput" />
      </div>

      <button class="btn btn-success" type="submit">Add Resource</button>
    </form>
  </div>
</template>

<script>
export default {
  inject: ["addResource"],
  data() {
    return {
      inputIsInvalid: false,
    };
  },
  methods: {
    submitData() {
      const enteredTitle = this.$refs.titleInput.value;
      const enteredDescription = this.$refs.descInput.value;
      const enteredLink = this.$refs.linkInput.value;

      if (enteredTitle.trim() === "" || enteredDescription.trim() === "" || enteredLink.trim() === "") {
        // trim to avoid empty blanks input spam
        this.inputIsInvalid = true;
        return; // return will stop the next line from executing
      }

      this.addResource(enteredTitle, enteredDescription, enteredLink);
    },
    confirmError() {
      this.inputIsInvalid = false;
    },
  },
};
</script>
