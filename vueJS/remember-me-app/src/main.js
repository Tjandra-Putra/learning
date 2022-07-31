import { createApp } from "vue";

import App from "./App.vue";
import BaseDialogue from "./components/UI/BaseDialogue.vue";

const app = createApp(App);

app.component("base-dialogue", BaseDialogue);

app.mount("#app");
