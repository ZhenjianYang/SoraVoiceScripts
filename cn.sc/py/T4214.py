from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4214   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4214.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '希尔丹夫人',                           # 9
        '茜亚',                                 # 10
        '布莉姆',                               # 11
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


    AddCharChip(
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02540 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
    )

    DeclNpc(
        X                   = 68000,
        Z                   = 0,
        Y                   = 69570,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 72500,
        Z                   = 0,
        Y                   = 67450,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 66670,
        Z                   = 0,
        Y                   = 99650,
        Direction           = 12,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_169",          # 01, 1
        "Function_2_18F",          # 02, 2
        "Function_3_30C",          # 03, 3
        "Function_4_330",          # 04, 4
        "Function_5_5A7",          # 05, 5
        "Function_6_C53",          # 06, 6
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_136")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_168")

    label("loc_136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_14A")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_168")

    label("loc_14A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_154")
    Jump("loc_168")

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_168")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168")
    SetChrFlags(0x8, 0x80)

    label("loc_168")

    Return()

    # Function_0_122 end

    def Function_1_169(): pass

    label("Function_1_169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_185")
    OP_B1("t4214_y")
    Jump("loc_18E")

    label("loc_185")

    OP_B1("t4214_n")

    label("loc_18E")

    Return()

    # Function_1_169 end

    def Function_2_18F(): pass

    label("Function_2_18F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2F6")

    label("loc_1B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2F6")

    label("loc_1CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2F6")

    label("loc_1E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2F6")

    label("loc_1FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2F6")

    label("loc_218")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2F6")

    label("loc_231")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2F6")

    label("loc_24A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_263")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2F6")

    label("loc_263")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2F6")

    label("loc_27C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2F6")

    label("loc_295")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2F6")

    label("loc_2AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2F6")

    label("loc_2C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2F6")

    label("loc_2E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2F6")

    label("loc_30B")

    Return()

    # Function_2_18F end

    def Function_3_30C(): pass

    label("Function_3_30C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32F")
    OP_8D(0xFE, 66030, 72430, 70230, 65960, 2000)
    Jump("Function_3_30C")

    label("loc_32F")

    Return()

    # Function_3_30C end

    def Function_4_330(): pass

    label("Function_4_330")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_54E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 7)), scpexpr(EXPR_END)), "loc_3D6")

    ChrTalk(    #0
        0xFE,
        (
            "……#0713F对凯诺娜小姐来说\x01",
            "上校就是一切。\x02\x03",

            "#0710F对她的心情和行为，\x01",
            "同样作为女性的我也\x01",
            "绝非不能理解……\x02\x03",

            "#0714F接下来就等女王\x01",
            "陛下来裁决吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54B")

    label("loc_3D6")


    ChrTalk(    #1
        0xFE,
        (
            "#0712F科洛蒂娅殿下和艾丝蒂尔小姐……\x02\x03",

            "#0710F……关于恐吓信那件事，看来\x01",
            "不只是单纯的恶作剧。\x02\x03",

            "想不到过去的情报部\x01",
            "竟然牵连在内……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1007F没错没错。\x02\x03",

            "#1015F想不到又和凯诺娜上尉\x01",
            "打了一回。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "……#0713F对凯诺娜小姐来说\x01",
            "上校就是一切。\x02\x03",

            "#0710F对她的心情和行为，\x01",
            "同样身为女性的我也\x01",
            "绝非不能理解……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        "#042F希尔丹夫人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "#0710F接下来就等女王\x01",
            "陛下来裁决吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1667)

    label("loc_54B")

    Jump("loc_5A3")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5A3")

    ChrTalk(    #6
        0xFE,
        (
            "#0712F想不到那位小姐\x01",
            "竟会变成这样……\x02\x03",

            "#0710F真希望她能快点\x01",
            "找到双亲……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A3")

    TalkEnd(0x8)
    Return()

    # Function_4_330 end

    def Function_5_5A7(): pass

    label("Function_5_5A7")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #7
        0xFE,
        "啊，约修亚先生……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1040F茜亚小姐，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "您能平安返回真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        "#1040F是茜亚？　感觉你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "你还是那么漂亮。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        "#1044F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "没、没什么。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6D9")

    label("loc_694")


    ChrTalk(    #15
        0xFE,
        (
            "科洛蒂娅殿下\x01",
            "去了谒见室哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "我想希尔丹夫人应该和她在一起。\x02",
    )

    CloseMessageWindow()

    label("loc_6D9")

    Jump("loc_C4F")

    label("loc_6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(    #17
        0xFE,
        (
            "签字仪式的准备外加这次的\x01",
            "善后处理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "真为女王陛下的身体担心……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C4F")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_END)), "loc_794")

    ChrTalk(    #19
        0xFE,
        (
            "各位似乎见到了\x01",
            "希尔丹夫人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "那个……方便的话要不要\x01",
            "我来准备些饮料呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4F")

    label("loc_794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_812")

    ChrTalk(    #21
        0xFE,
        "艾丝蒂尔小姐！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x105, 400)
    Sleep(600)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #22
        0xFE,
        "科洛蒂娅殿下和金先生也在！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_97B")

    label("loc_812")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_892")

    ChrTalk(    #23
        0xFE,
        "啊，科洛蒂娅殿下……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(600)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #24
        0xFE,
        "哎呀，艾丝蒂尔小姐和金先生也在！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_97B")

    label("loc_892")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_908")

    ChrTalk(    #25
        0xFE,
        "金先生！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x105, 400)
    Sleep(600)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #26
        0xFE,
        "科洛蒂娅殿下和艾丝蒂尔小姐也在！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_97B")

    label("loc_908")

    TurnDirection(0xFE, 0x105, 0)
    Sleep(600)

    ChrTalk(    #27
        0xFE,
        "科洛蒂娅殿下！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(600)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #28
        0xFE,
        "艾丝蒂尔小姐和金先生也在！？\x02",
    )

    CloseMessageWindow()

    label("loc_97B")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #29
        0xFE,
        (
            "真、真是失礼了……\x01",
            "久疏问候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x108,
        "#070F哈哈，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1001F嗯嗯，我还记得让茜亚小姐\x01",
            "给我们穿女佣装的事儿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x104,
        "#033F哟……艾丝蒂尔你穿女佣装？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1000F嗯，为了见到女王陛下。\x02\x03",

            "对了对了，还硬让\x01",
            "约修亚穿上了呢，\x01",
            "是茜亚小姐给他化的妆。\x02\x03",

            "#1001F那时候的茜亚小姐啊，\x01",
            "在化妆时好像很兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        "#044F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "不、不好意思……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x104,
        (
            "#037F完美扮演了塞茜莉亚\x01",
            "公主的约修亚的侍女身姿……\x02\x03",

            "啊，想必是\x01",
            "很可爱吧。\x02\x03",

            "#034F没能参加公爵的晚宴\x01",
            "真是我心中最大的懊恼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#045F呵呵……\x02\x03",

            "#040F对了对了，茜亚小姐，\x01",
            "你知道希尔丹夫人\x01",
            "去了哪里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "哦，希尔丹夫人现在\x01",
            "应该在资料室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "我记得她说有事\x01",
            "要调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1001F资料室啊，ＯＫ。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1629)
    Jump("loc_C4F")

    label("loc_C0D")


    ChrTalk(    #41
        0xFE,
        (
            "希尔丹夫人现在\x01",
            "应该在资料室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "我记得她说有事\x01",
            "要调查……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4F")

    TalkEnd(0x9)
    Return()

    # Function_5_5A7 end

    def Function_6_C53(): pass

    label("Function_6_C53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C7A")

    ChrTalk(    #43
        0xFE,
        (
            "呀！！\x01",
            "请、请别偷看～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7A")

    TalkEnd(0xFE)
    Return()

    # Function_6_C53 end

    SaveToFile()

Try(main)
