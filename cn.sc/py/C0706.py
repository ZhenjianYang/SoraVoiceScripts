from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0706   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0706.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_BE",           # 01, 1
        "Function_2_BF",           # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_BD")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_BD")

    Return()

    # Function_0_AA end

    def Function_1_BE(): pass

    label("Function_1_BE")

    Return()

    # Function_1_BE end

    def Function_2_BF(): pass

    label("Function_2_BF")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-32090, 30000, -26260, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(45000, 0)
    OP_6E(343, 0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(80, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #0
        "\x07\x00#1020F那、那是什么……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(160, 320, -1, -1)
    SetChrName("凯文神父")

    AnonymousTalk(    #1
        (
            "\x07\x00#1063F和那个『福音』产生的\x01",
            "黑色波动的状态很像，不过……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 310, -1, -1)
    SetChrName("拉赛尔博士")

    AnonymousTalk(    #2
        (
            "\x07\x00#102F但是，和波动不同的是没有扩展开来\x01",
            "而是笼罩了整个塔顶。\x02\x03",

            "不管怎样，还是不要\x01",
            "再接近为妙。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FA)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_2_BF end

    SaveToFile()

Try(main)
