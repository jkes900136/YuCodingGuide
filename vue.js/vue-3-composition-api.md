# Vue 3 Composition API

Composition API算是Vue3帶來新的元件(component)實作方式，且不僅Vue3以上的版本能使用，也可以在Vue2.7以上的版本直接撰寫。

如果使用Vue2.6(含)以下的版本呢？

@vue/composition-api就是舊專案的救星，只要以npm安裝它，古蹟維護不再是難事～

```powershell
npm install @vue/composition-api
```

至於一般開發，只在單一檔案元件Single-File Components (SFCs)編寫邏輯程式碼的話，僅須將邏輯寫在\<script setup>內，畫面元件則定義在\<template>內。

如此程式碼就顯得簡潔~~有力~~\~

```html
<script setup>
import { ref, onMounted } from 'vue'
// reactive state
const count = ref(0)

// functions that mutate state and trigger updates
function increment() {
  count.value++
}

// lifecycle hooks
onMounted(() => {
  console.log(`The initial count is ${count.value}.`)
})
</script>
<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

setup實作上有不同形式，若要跨檔案元件開發程式的話，就須要將setup以函數的形式單獨撰寫。

```html
<script>
import { reactive } from 'vue'

export default {
  setup() {
    const state = reactive({ count: 0 })

    function increment() {
      state.count++
    }

    // don't forget to expose the function as well.
    return {
      state,
      increment
    }
  }
}
</script>
<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

#### props 和 emits&#x20;

以props接受外部參數，透過emits回拋參數

```typescript
props:['id'], 
setup(props, context) { 
console.log(props.id) // 接受參數 
context.emit('done'); // 回拋參數
}
```

#### 好用的watch

當外部元件的變數有變化時，我們撰寫的程式也能很聰明\~ &#x20;

```typescript
  watch(id, (newValue, oldValue) => { // 監看參數 
  }); 
  watch(()=>obj.id, (newValue, oldValue) => { // 監看物件
   });
 watchEffect(() => { // 自動監看使用到的變數 
 fetchData(); // 只要 props的id 有變化，就會自動執行 fetchData()
 // 若 props的id 包在特定的JavaScript原生語法內裡面，則無作用
  }) 
 
 const fetchData = () => { 
     if (props.id){         
        ...            
      }
  }
```
