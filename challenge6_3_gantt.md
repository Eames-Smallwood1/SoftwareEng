# Gantt


``` mermaid

gantt
    title Online-Pizza Ordering System — 10-Day Project Timeline
    dateFormat YYYY-MM-DD
    axisFormat %b %d

    section Project Management 
    Planning and scheduling          :plan, 2026-11-05, 1d
    Status reporting                 :2026-11-06, 9d

    section Requirements and Design 
    Requirements gathering           :req, 2026-11-05, 1d
    UX design                        :ux, after req, 1d
    Architecture and database design :arch, after req, 1d

    section Customer Web Application 
    Menu browsing                    :menu, after ux arch, 1d
    Pizza customization              :custom, after menu, 2d
    Shopping cart                    :cart, after custom, 1d
    Checkout and payment             :checkout, after cart orders, 1d
    Account and order tracking       :account, after auth orders, 2d

    section Back-End Services 
    Menu and pricing service         :pricing, after arch, 1d
    Order service                    :orders, after pricing, 2d
    Authentication and security      :auth, after arch, 2d

    section Restaurant Staff Tools 
    Order queue dashboard            :queue, after orders, 2d
    Menu management                  :manage, after pricing auth, 2d

    section Testing 
    Automated tests                  :auto, after menu pricing, 5d
    Usability and security testing   :qa, after checkout account queue manage auto, 1d

    section Deployment and Launch 
    Hosting and CI/CD setup          :hosting, after arch, 2d
    Launch and support               :launch, after qa hosting, 1d

```