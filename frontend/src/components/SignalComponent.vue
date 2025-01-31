<template>
    <div>
      <textarea v-model="signal" placeholder="Enter signal data as comma-separated values"></textarea>
      <button @click="submitSignal">Analyze</button>
      
      <div v-if="result">
        <h3>Analysis Result:</h3>
        <p><strong>Max value:</strong> {{ result.max }}</p>
        <p><strong>Min value:</strong> {{ result.min }}</p>
        <p><strong>Mean value:</strong> {{ result.mean }}</p>
        <p><strong>Standard deviation:</strong> {{ result.std_dev }}</p>
        <p><strong>Mean PSD:</strong> {{ result.psd_mean }}</p>
        <p><strong>Max PSD:</strong> {{ result.psd_max }}</p>
        <p v-if="result.error">{{ result.error }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        signal: '',
        result: null
      };
    },
    methods: {
        async submitSignal() {
            try {
                const response = await fetch("http://localhost:8000/analyze_signal", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"  // Убедись, что ты указал правильный заголовок
                },
                body: JSON.stringify({ signal: this.signal })  // Отправляешь данные сигнала в формате JSON
                });
                
                if (!response.ok) {
                throw new Error('Failed to analyze signal');
                }
                
                // Обрабатываем результат, если запрос успешен
                this.result = await response.json();
            } catch (error) {
                console.error('Error during signal analysis:', error);
            }
        }
    }
  };
  </script>  