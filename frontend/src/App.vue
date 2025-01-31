<template>
  <div id="app">
    <h1>Medical Signal Analysis</h1>
    <SignalComponent />
  </div>
</template>

<script>
import SignalComponent from './components/SignalComponent.vue'

export default {
  name: 'App',
  components: {
    SignalComponent
  }
}
</script>