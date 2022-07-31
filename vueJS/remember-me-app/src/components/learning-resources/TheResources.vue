<template>
  <div class="container mt-4">
    <nav>
      <div class="nav nav-tabs mb-4" id="nav-tab" role="tablist">
        <button class="nav-link" :class="storedResButtonMode" @click="setSelectedTab('stored-resources')">
          Stored Resources
        </button>
        <button class="nav-link" :class="addResButtonMode" @click="setSelectedTab('add-resource')">
          Add Resources
        </button>
      </div>
    </nav>

    <keep-alive>
      <component :is="selectedTab"></component>
    </keep-alive>
  </div>
</template>

<script>
import StoredResources from "./StoredResources.vue";
import AddResource from "./AddResource.vue";

export default {
  components: {
    StoredResources,
    AddResource,
  },
  data() {
    return {
      selectedTab: "stored-resources",
      lactive: "active",
      ractive: "",
      storedResourcesArr: [
        {
          id: "official-guide",
          title: "Official Guide",
          description: "The official Vue.js documentation.",
          link: "https://vuejs.org",
        },
        {
          id: "google",
          title: "Google",
          description: "Learn to google...",
          link: "https://google.com",
        },
      ],
    };
  },
  provide() {
    return {
      resources: this.storedResourcesArr,
      addResource: this.addResource,
      deleteResource: this.removeResource,
    };
  },
  computed: {
    storedResButtonMode() {
      return this.selectedTab === "stored-resources" ? "active" : "";
    },
    addResButtonMode() {
      return this.selectedTab === "add-resource" ? "active" : "";
    },
  },
  methods: {
    setSelectedTab(tab) {
      this.selectedTab = tab;
    },
    addResource(title, description, url) {
      const newResource = {
        id: new Date().toISOString(),
        title: title,
        description: description,
        link: url,
      };
      this.storedResourcesArr.unshift(newResource); // push to beginning of the array
      this.selectedTab = "stored-resources"; // switch tab
    },
    removeResource(resId) {
      const resIndex = this.storedResourcesArr.findIndex((res) => res.id === resId);
      this.storedResourcesArr.splice(resIndex, 1); // remove one element based on the id
    },
  },
};
</script>
