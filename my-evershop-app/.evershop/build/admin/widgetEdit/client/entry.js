
      import React from 'react';
      import ReactDOM from 'react-dom';
      import { Area } from '@evershop/evershop/components/common';
      import {HydrateAdmin} from '@evershop/evershop/components/common';
      
import eaa8834c237293b6a1cbd0ca54ee8d395 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/auth/pages/admin/all/AdminUser.js';
import ef331b0cc39db2deb05174211ac21df62 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/catalog/pages/admin/all/CatalogMenuGroup.js';
import e8acf8e1fa2f60239578835c74810c6f8 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/catalog/pages/admin/all/NewProductQuickLink.js';
import e2445ff46f69b100b11c2aae5d9c08974 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/checkout/pages/admin/all/ShippingSettingMenu.js';
import e144e56aa40c9f714b5625bbf503da3c6 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/CmsMenuGroup.js';
import eb277b8f5a56eb93582ff7f0f2cc388d2 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/CopyRight.js';
import eba3b7f57398de8c18845fa1db7d14fc6 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/Layout.js';
import e8950258c14103c64d56b5aedd7d463bd from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/Logo.js';
import ee8add0a66ab342194ee3662f86fa1184 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/Meta.js';
import e502bd90741dce43173be2fc05077fbe7 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/Navigation.js';
import e2f0fdaf690129dd76ba622247571316e from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/Notification.js';
import e49ac4e134c4059ccb6c572c7498f3211 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/QuickLinks.js';
import e562a998c97dd872edb762ad1dfe7ba66 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/SearchBox.js';
import efa110c19510f43785821ee6943ec2a20 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/all/Version.js';
import ea0fda778bef464cd8a1912d495b2adc7 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/widgetEdit/WidgetForm.js';
import ee8b3bd1137fa0de26b0295a827fc39b2 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/widgetEdit+widgetNew/FormContent.js';
import e33e82190f96665bca75c16b53579138b from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/widgetEdit+widgetNew/General.js';
import e8f6681cdbfec79196ce3261e6f07473e from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/widgetEdit+widgetNew/PageHeading.js';
import e227b9c52b46b94bc846b9242dfbf7220 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/cms/pages/admin/widgetEdit+widgetNew/Setting.js';
import e1eb1bf231bf46c4ef18c0e1300555b21 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/customer/pages/admin/all/CustomerMenuGroup.js';
import eb06215a2139cdee901ff4aeaf8014a87 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/oms/pages/admin/all/OmsMenuGroup.js';
import eaaf4ae12deda66068970d6e97fdd85f2 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/promotion/pages/admin/all/CouponMenuGroup.js';
import e5867f73727c7faf28d332d7182e25b47 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/promotion/pages/admin/all/NewCouponQuickLink.js';
import e3a87e690126bd2a6ea36b6f7f26af8d4 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/setting/pages/admin/all/PaymentSettingMenu.js';
import e04670defd1c4471adcb98202a4f6546b from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/setting/pages/admin/all/SettingMenuGroup.js';
import e01cf8b124046803c7fbb4572fd96dac6 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/setting/pages/admin/all/StoreSettingMenu.js';
import e4b60b185d0e1bc726ff0d5defcdf43f7 from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/modules/tax/pages/admin/all/TaxSettingMenu.js';
import e20ba607afcc81175becb8399291b711e from 'file:///C:/IRWAproject/my-evershop-app/extensions/sample/dist/pages/admin/all/Hello.js';
import collection_products from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/components/admin/widgets/CollectionProductsSetting.js';
import text_block from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/components/admin/widgets/TextBlockSetting.js';
import basic_menu from 'file:///C:/IRWAproject/my-evershop-app/node_modules/@evershop/evershop/dist/components/admin/widgets/BasicMenuSetting.js';
Area.defaultProps.components = {
  header: {
    eaa8834c237293b6a1cbd0ca54ee8d395: {
      id: 'eaa8834c237293b6a1cbd0ca54ee8d395',
      sortOrder: 50,
      component: { default: eaa8834c237293b6a1cbd0ca54ee8d395 }
    },
    e8950258c14103c64d56b5aedd7d463bd: {
      id: 'e8950258c14103c64d56b5aedd7d463bd',
      sortOrder: 10,
      component: { default: e8950258c14103c64d56b5aedd7d463bd }
    },
    e562a998c97dd872edb762ad1dfe7ba66: {
      id: 'e562a998c97dd872edb762ad1dfe7ba66',
      sortOrder: 20,
      component: { default: e562a998c97dd872edb762ad1dfe7ba66 }
    }
  },
  adminMenu: {
    ef331b0cc39db2deb05174211ac21df62: {
      id: 'ef331b0cc39db2deb05174211ac21df62',
      sortOrder: 20,
      component: { default: ef331b0cc39db2deb05174211ac21df62 }
    },
    e144e56aa40c9f714b5625bbf503da3c6: {
      id: 'e144e56aa40c9f714b5625bbf503da3c6',
      sortOrder: 60,
      component: { default: e144e56aa40c9f714b5625bbf503da3c6 }
    },
    e49ac4e134c4059ccb6c572c7498f3211: {
      id: 'e49ac4e134c4059ccb6c572c7498f3211',
      sortOrder: 10,
      component: { default: e49ac4e134c4059ccb6c572c7498f3211 }
    },
    e1eb1bf231bf46c4ef18c0e1300555b21: {
      id: 'e1eb1bf231bf46c4ef18c0e1300555b21',
      sortOrder: 40,
      component: { default: e1eb1bf231bf46c4ef18c0e1300555b21 }
    },
    eb06215a2139cdee901ff4aeaf8014a87: {
      id: 'eb06215a2139cdee901ff4aeaf8014a87',
      sortOrder: 30,
      component: { default: eb06215a2139cdee901ff4aeaf8014a87 }
    },
    eaaf4ae12deda66068970d6e97fdd85f2: {
      id: 'eaaf4ae12deda66068970d6e97fdd85f2',
      sortOrder: 50,
      component: { default: eaaf4ae12deda66068970d6e97fdd85f2 }
    },
    e04670defd1c4471adcb98202a4f6546b: {
      id: 'e04670defd1c4471adcb98202a4f6546b',
      sortOrder: 500,
      component: { default: e04670defd1c4471adcb98202a4f6546b }
    }
  },
  quickLinks: {
    e8acf8e1fa2f60239578835c74810c6f8: {
      id: 'e8acf8e1fa2f60239578835c74810c6f8',
      sortOrder: 20,
      component: { default: e8acf8e1fa2f60239578835c74810c6f8 }
    },
    e5867f73727c7faf28d332d7182e25b47: {
      id: 'e5867f73727c7faf28d332d7182e25b47',
      sortOrder: 30,
      component: { default: e5867f73727c7faf28d332d7182e25b47 }
    }
  },
  settingPageMenu: {
    e2445ff46f69b100b11c2aae5d9c08974: {
      id: 'e2445ff46f69b100b11c2aae5d9c08974',
      sortOrder: 15,
      component: { default: e2445ff46f69b100b11c2aae5d9c08974 }
    },
    e3a87e690126bd2a6ea36b6f7f26af8d4: {
      id: 'e3a87e690126bd2a6ea36b6f7f26af8d4',
      sortOrder: 10,
      component: { default: e3a87e690126bd2a6ea36b6f7f26af8d4 }
    },
    e01cf8b124046803c7fbb4572fd96dac6: {
      id: 'e01cf8b124046803c7fbb4572fd96dac6',
      sortOrder: 5,
      component: { default: e01cf8b124046803c7fbb4572fd96dac6 }
    },
    e4b60b185d0e1bc726ff0d5defcdf43f7: {
      id: 'e4b60b185d0e1bc726ff0d5defcdf43f7',
      sortOrder: 20,
      component: { default: e4b60b185d0e1bc726ff0d5defcdf43f7 }
    }
  },
  footerLeft: {
    eb277b8f5a56eb93582ff7f0f2cc388d2: {
      id: 'eb277b8f5a56eb93582ff7f0f2cc388d2',
      sortOrder: 10,
      component: { default: eb277b8f5a56eb93582ff7f0f2cc388d2 }
    },
    efa110c19510f43785821ee6943ec2a20: {
      id: 'efa110c19510f43785821ee6943ec2a20',
      sortOrder: 20,
      component: { default: efa110c19510f43785821ee6943ec2a20 }
    }
  },
  body: {
    eba3b7f57398de8c18845fa1db7d14fc6: {
      id: 'eba3b7f57398de8c18845fa1db7d14fc6',
      sortOrder: 10,
      component: { default: eba3b7f57398de8c18845fa1db7d14fc6 }
    },
    e2f0fdaf690129dd76ba622247571316e: {
      id: 'e2f0fdaf690129dd76ba622247571316e',
      sortOrder: 10,
      component: { default: e2f0fdaf690129dd76ba622247571316e }
    }
  },
  head: {
    ee8add0a66ab342194ee3662f86fa1184: {
      id: 'ee8add0a66ab342194ee3662f86fa1184',
      sortOrder: 5,
      component: { default: ee8add0a66ab342194ee3662f86fa1184 }
    }
  },
  adminNavigation: {
    e502bd90741dce43173be2fc05077fbe7: {
      id: 'e502bd90741dce43173be2fc05077fbe7',
      sortOrder: 10,
      component: { default: e502bd90741dce43173be2fc05077fbe7 }
    }
  },
  content: {
    ea0fda778bef464cd8a1912d495b2adc7: {
      id: 'ea0fda778bef464cd8a1912d495b2adc7',
      sortOrder: 10,
      component: { default: ea0fda778bef464cd8a1912d495b2adc7 }
    },
    e8f6681cdbfec79196ce3261e6f07473e: {
      id: 'e8f6681cdbfec79196ce3261e6f07473e',
      sortOrder: 5,
      component: { default: e8f6681cdbfec79196ce3261e6f07473e }
    },
    e20ba607afcc81175becb8399291b711e: {
      id: 'e20ba607afcc81175becb8399291b711e',
      sortOrder: 0,
      component: { default: e20ba607afcc81175becb8399291b711e }
    }
  },
  widgetForm: {
    ee8b3bd1137fa0de26b0295a827fc39b2: {
      id: 'ee8b3bd1137fa0de26b0295a827fc39b2',
      sortOrder: 10,
      component: { default: ee8b3bd1137fa0de26b0295a827fc39b2 }
    }
  },
  rightSide: {
    e33e82190f96665bca75c16b53579138b: {
      id: 'e33e82190f96665bca75c16b53579138b',
      sortOrder: 15,
      component: { default: e33e82190f96665bca75c16b53579138b }
    }
  },
  leftSide: {
    e227b9c52b46b94bc846b9242dfbf7220: {
      id: 'e227b9c52b46b94bc846b9242dfbf7220',
      sortOrder: 30,
      component: { default: e227b9c52b46b94bc846b9242dfbf7220 }
    }
  },
  '*': {
    collection_products: {
      id: 'collection_products',
      sortOrder: 0,
      component: { default: collection_products }
    },
    text_block: {
      id: 'text_block',
      sortOrder: 0,
      component: { default: text_block }
    },
    basic_menu: {
      id: 'basic_menu',
      sortOrder: 0,
      component: { default: basic_menu }
    }
  }
} 
ReactDOM.hydrate(
        React.createElement(HydrateAdmin, null),
        document.getElementById('app')
      );