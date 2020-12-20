## Nodinx的中台职能

结合目前的 AISee 系统，大量业务处理渗透到 Java 服务中，系统中台 [Nodinx](http://nodinx.sparta.html5.qq.com/zh-cn/intro/index.html)（基于 EggJS 和 Koa.js 封装）一开始的设计旨在提供 HTTP 接入层，随着业务成长和迭代，自身作为业务中台的技术地位越来越明显。

Nodinx 对 HTTP 请求依然延用 Koa.js 的洋葱圈模型处理。

![](./imgs/model.png)

那么目前的 AISee Nodinx 服务做了哪些事情

1. [nodinx-cas](https://git.code.oa.com/WSRD-Tech-Center-Lib/nodinx-cas)

  单点登录接管用户请求方行为 
  
2. [nodinx-taf-proxy](https://git.code.oa.com/WSRD-Tech-Center-Lib/nodinx-taf-proxy)

  提供 proxy 基于 tcp 协议调用 taf
  
3. 提供前排 HTTP 接口，拼装细粒度 Java Taf 接口组装业务逻辑

4. 接入端提供 API 服务，管理端提供 Open API

5. [Swagger 文档服务](http://aisee.oa.com/swagger)

6. 日志管理

7. 测试用例管理和覆盖率扫描

8. [nodinx-validate](https://git.code.oa.com/WSRD-Tech-Center-Lib/nodinx-validate)

  业务接口的参数校验（目前业务中已经被 [Joi](https://hapi.dev/family/joi/) 取代）

9. 对前端页面输出 view model，适配不同页面业务场景的数据模型

10. [nodinx-mock](https://git.code.oa.com/WSRD-Tech-Center-Lib/nodinx-mock)
  
  针对 HTTP 的中台 Mock

而 Nodinx 本身的设计遵守 __约定大于配置__ 的规范，其内部通过插件的形式做了很多隐式的封装，譬如

1. nodinx-seer-router

  生产环境主控寻址

2. [nodinx-frequency](https://git.code.oa.com/WSRD-Tech-Center-Lib/nodinx-frequency)

  处理针对 userId 和 token 不同请求特征组合的频次限流处理

3. [nodinx-security](https://git.code.oa.com/WSRD-Tech-Center-Lib/nodinx-security)

  针对页面跨域和内容安全进行配置和管理

4. [nodinx-errors](https://git.code.oa.com/WSRD-Tech-Center-Lib/nodinx-errors)

  中台统一错误码管理

......