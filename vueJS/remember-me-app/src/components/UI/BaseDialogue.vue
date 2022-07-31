<template>
  <teleport to="body">
    <div @click="$emit('close')"></div>
    <dialog open>
      <header>
        <slot name="header">
          <h2>{{ title }}</h2>
        </slot>
      </header>
      <section>
        <slot></slot>
      </section>
      <menu>
        <slot name="actions">
          <button class="btn btn-dark" @click="$emit('close')">Close</button>
        </slot>
      </menu>
    </dialog>
  </teleport>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false,
    },
  },
  emits: ["close"],
};
</script>

<style scoped>
@media (min-width: 768px) {
  div {
    position: fixed;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100%;
    background: rgba(0, 0, 0, 0.75);
    z-index: 10;
  }
  dialog {
    overflow: hidden;
    margin: 0;
    padding: 0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    border: none;
    border-radius: 12px;
    z-index: 100;
    width: 80%;
    left: 28%;
    top: 25vh;
    position: absolute;
    width: 40rem;
  }
  header {
    background: #3a0061;
    color: white;
    width: 100%;
    padding: 1rem;
  }
  header h2 {
    margin: 0;
  }
  section {
    padding: 1rem;
  }
  menu {
    padding: 1rem;
    display: flex;
    justify-content: flex-end;
    margin: 0;
  }
}
</style>
