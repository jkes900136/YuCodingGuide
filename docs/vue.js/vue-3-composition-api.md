# Vue 3 Composition API

Composition APIç®—æ˜¯Vue3å¸¶ä??°ç??ƒä»¶(component)å¯¦ä??¹å?ï¼Œä?ä¸å?Vue3ä»¥ä??„ç??¬èƒ½ä½¿ç”¨ï¼Œä??¯ä»¥?¨Vue2.7ä»¥ä??„ç??¬ç›´?¥æ’°å¯«ã€?

å¦‚æ?ä½¿ç”¨Vue2.6(??ä»¥ä??„ç??¬å‘¢ï¼?

@vue/composition-apiå°±æ˜¯?Šå?æ¡ˆç??‘æ?ï¼Œåªè¦ä»¥npmå®‰è?å®ƒï??¤è?ç¶­è­·ä¸å??¯é›£äº‹ï?

```powershell
npm install @vue/composition-api
```

?³æ–¼ä¸€?¬é??¼ï??ªåœ¨?®ä?æª”æ??ƒä»¶Single-File Components (SFCs)ç·¨å¯«?è¼¯ç¨‹å?ç¢¼ç?è©±ï??…é?å°‡é?è¼¯å¯«?¨\<script setup>?§ï??«é¢?ƒä»¶?‡å?ç¾©åœ¨\<template>?§ã€?

å¦‚æ­¤ç¨‹å?ç¢¼å°±é¡¯å?ç°¡æ?~~?‰å?~~\~

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

setupå¯¦ä?ä¸Šæ?ä¸å?å½¢å?ï¼Œè‹¥è¦è·¨æª”æ??ƒä»¶?‹ç™¼ç¨‹å??„è©±ï¼Œå°±?ˆè?å°‡setupä»¥å‡½?¸ç?å½¢å??®ç¨?°å¯«??

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

#### props ??emits&#x20;

ä»¥props?¥å?å¤–éƒ¨?ƒæ•¸ï¼Œé€é?emits?æ??ƒæ•¸

```typescript
props:['id'], 
setup(props, context) { 
console.log(props.id) // ?¥å??ƒæ•¸ 
context.emit('done'); // ?æ??ƒæ•¸
}
```

#### å¥½ç”¨?„watch

?¶å??¨å?ä»¶ç?è®Šæ•¸?‰è??–æ?ï¼Œæ??‘æ’°å¯«ç?ç¨‹å?ä¹Ÿèƒ½å¾ˆè°?\~ &#x20;

```typescript
  watch(id, (newValue, oldValue) => { // ????ƒæ•¸ 
  }); 
  watch(()=>obj.id, (newValue, oldValue) => { // ????©ä»¶
   });
 watchEffect(() => { // ?ªå????ä½¿ç”¨?°ç?è®Šæ•¸ 
 fetchData(); // ?ªè? props?„id ?‰è??–ï?å°±æ??ªå??·è? fetchData()
 // ??props?„id ?…åœ¨?¹å??„JavaScript?Ÿç?èªæ??§è£¡?¢ï??‡ç„¡ä½œç”¨
  }) 
 
 const fetchData = () => { 
     if (props.id){         
        ...            
      }
  }
```
