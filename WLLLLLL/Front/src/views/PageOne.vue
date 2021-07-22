<template>
  <div class="wrapper">
    <div class="header">header</div>
    <div class="main">main</div>
    <div class="footer">footer</div>
  </div>

</template>

<style>

.wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100%;
}

.header {
  flex: 0;
}

.main{
  flex: 1;
}

.footer {
  flex: 0;
}
</style>
