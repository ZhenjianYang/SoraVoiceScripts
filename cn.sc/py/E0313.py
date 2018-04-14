from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0313   ._SN',
        MapName             = 'Event',
        Location            = 'E0313.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
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
        '菲',                                   # 9
        '修理员佩顿',                           # 10
        '亲卫队队员',                           # 11
        '亲卫队队员',                           # 12
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
        'ED6_DT07/CH01550 ._CH',             # 00
        'ED6_DT07/CH01450 ._CH',             # 01
        'ED6_DT07/CH01320 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01550P._CP',             # 00
        'ED6_DT07/CH01450P._CP',             # 01
        'ED6_DT07/CH01320P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2270,
        Z                   = 0,
        Y                   = 5880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 2820,
        Z                   = 0,
        Y                   = -90,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 2280,
        Z                   = 0,
        Y                   = 6070,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclEvent(
        X                   = 700,
        Y                   = -2000,
        Z                   = -10500,
        Range               = 3200,
        Unknown_10          = 0xDAC,
        Unknown_14          = 0xFFFFE2B4,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = -30,
        Y                   = -1000,
        Z                   = -7340,
        Range               = 3700,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFDC88,
        Unknown_18          = 0x0,
        Unknown_1C          = 27,
    )


    ScpFunction(
        "Function_0_182",          # 00, 0
        "Function_1_217",          # 01, 1
        "Function_2_3A2",          # 02, 2
        "Function_3_3B8",          # 03, 3
        "Function_4_BFE",          # 04, 4
        "Function_5_112F",         # 05, 5
        "Function_6_128A",         # 06, 6
        "Function_7_16BA",         # 07, 7
        "Function_8_1C65",         # 08, 8
        "Function_9_1DA4",         # 09, 9
        "Function_10_1F58",        # 0A, 10
        "Function_11_212F",        # 0B, 11
        "Function_12_2306",        # 0C, 12
        "Function_13_24DD",        # 0D, 13
        "Function_14_26B4",        # 0E, 14
        "Function_15_2891",        # 0F, 15
        "Function_16_2A6E",        # 10, 16
        "Function_17_2B41",        # 11, 17
        "Function_18_2B5D",        # 12, 18
        "Function_19_2B79",        # 13, 19
        "Function_20_2B95",        # 14, 20
        "Function_21_2BC5",        # 15, 21
        "Function_22_2BE1",        # 16, 22
        "Function_23_2C1A",        # 17, 23
        "Function_24_2CA1",        # 18, 24
        "Function_25_2D30",        # 19, 25
        "Function_26_2DBD",        # 1A, 26
        "Function_27_2E4A",        # 1B, 27
    )


    def Function_0_182(): pass

    label("Function_0_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_1CF")

    label("loc_199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4")
    Jump("loc_1CF")

    label("loc_1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_1CF")

    label("loc_1B4")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3690, 0, -4710, 90)

    label("loc_1CF")

    Jump("loc_203")

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_1F2")
    SetChrPos(0x8, 3690, 0, -4710, 90)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_203")

    label("loc_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_203")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_216")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_216")

    Return()

    # Function_0_182 end

    def Function_1_217(): pass

    label("Function_1_217")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_235")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_265")
    OP_B1("E0313_1")
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x8)
    OP_6F(0x5, 0)
    Jump("loc_26E")

    label("loc_265")

    OP_B1("E0313_2")

    label("loc_26E")

    Jump("loc_2A3")

    label("loc_271")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289")
    OP_B1("E0313_2")
    Jump("loc_2A3")

    label("loc_289")

    OP_B1("E0313_1")
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x8)
    OP_6F(0x5, 0)

    label("loc_2A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CC")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D9")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9")
    OP_22(0x7A, 0x1, 0x46)

    label("loc_2D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_304")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x7A, 0x1, 0x46)

    label("loc_304")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_325")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_32C")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_34A")
    OP_71(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    Jump("loc_3A1")

    label("loc_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_368")
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x9, 0x4)
    Jump("loc_3A1")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_386")
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_72(0x9, 0x4)
    Jump("loc_3A1")

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_3A1")
    OP_72(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)

    label("loc_3A1")

    Return()

    # Function_1_217 end

    def Function_2_3A2(): pass

    label("Function_2_3A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3A2")

    label("loc_3B7")

    Return()

    # Function_2_3A2 end

    def Function_3_3B8(): pass

    label("Function_3_3B8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_3D7")

    ChrTalk(    #0
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BFA")

    label("loc_3D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EA")
    Call(0, 14)
    Jump("loc_BFA")

    label("loc_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FD")
    Call(0, 12)
    Jump("loc_BFA")

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_410")
    Call(0, 10)
    Jump("loc_BFA")

    label("loc_410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F")
    Call(0, 7)
    Jump("loc_BFA")

    label("loc_41F")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【说话】\x01",            # 0
            "【搭乘升降机】\x01",      # 1
            "【放弃】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_556")

    ChrTalk(    #1
        0xFE,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "那么请立刻\x01",
            "站到升降机上吧。\x02",
        )
    )

    CloseMessageWindow()
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_4E6")
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_552")

    label("loc_4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_50B")
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_552")

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_530")
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_552")

    label("loc_530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_552")
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_552")

    Return()

    label("loc_556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_567")
    TalkEnd(0xFE)
    Return()

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_68A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")

    ChrTalk(    #3
        0xFE,
        (
            "博士正在研究的『装置』\x01",
            "试制终于有了头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "用升降机将你们送下去之后，\x01",
            "我要马上去帮忙进行原型的制作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "嗯，它的功能大概要等到\x01",
            "组装完毕后才会知道呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_687")

    label("loc_61D")


    ChrTalk(    #6
        0xFE,
        (
            "『装置』有了试作的头绪，\x01",
            "我也打算过去帮一下忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "嗯，至于有些什么功能，\x01",
            "这就是组装完毕后的事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_687")

    Jump("loc_BFA")

    label("loc_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_7A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_742")

    ChrTalk(    #8
        0xFE,
        (
            "刚才中央工房的雷伊\x01",
            "一边散步一边发着牢骚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "他一直都很沉着冷静，\x01",
            "从来就不是那种埋首研究的类型……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "不过他居然变成那样，\x01",
            "看来这次的研究似乎相当困难呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_7A6")

    label("loc_742")


    ChrTalk(    #11
        0xFE,
        (
            "刚才中央工房的雷伊\x01",
            "一边散步一边发着牢骚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "他居然变成那样，\x01",
            "看来这次的研究似乎相当困难呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A6")

    Jump("loc_BFA")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_8EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875")

    ChrTalk(    #13
        0xFE,
        (
            "拉赛尔老爷子所研究的东西\x01",
            "好像是极特殊的导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "我看过设计图，但是里面有一大堆\x01",
            "功能不明的结晶回路，真令人头疼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "乍看很像是导力波的增幅器……\x01",
            "到底是用来做什么的装置呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_8E7")

    label("loc_875")


    ChrTalk(    #16
        0xFE,
        (
            "拉赛尔老爷子所研究的东西\x01",
            "好像是极特殊的导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "乍看很像是导力波的增幅器……\x01",
            "到底是用来做什么的装置呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E7")

    Jump("loc_BFA")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_BFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B98")

    ChrTalk(    #18
        0xFE,
        (
            "虽然我不太清楚详情，\x01",
            "不过好像是老爷子正在研究新发明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "所以，因为人手不够\x01",
            "急急忙忙叫我们来凑数是吗。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97C")
    OP_A2(0x3)

    label("loc_97C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F4")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇前作『爱的使者』高评价完成】\x01",      # 0
            "【◇没有完成】\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9E8"),
        (1, "loc_9EE"),
        (SWITCH_DEFAULT, "loc_9F4"),
    )


    label("loc_9E8")

    OP_A2(0x3)
    Jump("loc_9F4")

    label("loc_9EE")

    OP_A3(0x3)
    Jump("loc_9F4")

    label("loc_9F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A31")

    ChrTalk(    #20
        0xFE,
        (
            "呼～，本来这个时候\x01",
            "应该正在和布拉姆旅行呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A62")

    label("loc_A31")


    ChrTalk(    #21
        0xFE,
        (
            "呼～，本来这个时候\x01",
            "应该正在和鲁迪旅行呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC1")

    ChrTalk(    #22
        0x107,
        (
            "#562F啊……\x01",
            "菲小姐，真的很抱歉。\x02\x03",

            "一直以来都是\x01",
            "因为爷爷的缘故……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)
    Jump("loc_AF9")

    label("loc_AC1")


    ChrTalk(    #23
        0x101,
        (
            "#1016F啊、啊哈哈……\x01",
            "让人不禁有点同情你呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    label("loc_AF9")


    ChrTalk(    #24
        0xFE,
        (
            "不过，在这种时候受人之托\x01",
            "心里还是很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "而且这项工作也十分有意义，\x01",
            "我可不会对那些小事耿耿于怀哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "有什么难处要告诉我啊。\x01",
            "我会帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_BFA")

    label("loc_B98")


    ChrTalk(    #27
        0xFE,
        (
            "拉赛尔老爷子\x01",
            "好像在研究什么新发明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "光是分析塔的现象就够忙了，\x01",
            "居然还在插手其它的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFA")

    TalkEnd(0x8)
    Return()

    # Function_3_3B8 end

    def Function_4_BFE(): pass

    label("Function_4_BFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_112B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【决定做在◇3章中没遇到的事】\x01",      # 0
            "【决定做在◇3章中见到过的事】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF2")

    ChrTalk(    #29
        0xFE,
        (
            "呀，艾丝蒂尔。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1015F啊，你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "咦，不记得我了吗？\x01",
            "我是维修员佩顿啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "理查德上校事件发生时\x01",
            "我曾经参加了作战啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1008F对、对不起。\x01",
            "终于想起来了。\x02\x03",

            "就是那个时候为我们\x01",
            "准备了特务艇的人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "啊哈哈，谢谢。\x01",
            "你能想起我是我的光荣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "不过，我听别人说\x01",
            "有游击士要登舰……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "不过没想到\x01",
            "是艾丝蒂尔你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EDB")

    label("loc_DF2")


    ChrTalk(    #37
        0xFE,
        "哎呀，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1004F啊，佩顿先生。\x01",
            "你怎么会在这里呢？\x02\x03",

            "#1016F……不过仔细想想\x01",
            "也是理所当然的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "啊哈哈，因为我可是\x01",
            "这艘军舰的专职维修员啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "不过，我听别人说\x01",
            "有游击士要登舰……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "不过没想到\x01",
            "是艾丝蒂尔你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDB")


    ChrTalk(    #42
        0x101,
        (
            "#1006F我也没想到\x01",
            "『埃尔赛尤』会来。\x02\x03",

            "看来王国军对于这次作战\x01",
            "投入了相当多的力量呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "是啊，听说是继『百日战役』之后，\x01",
            "最大的作战行动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "还有，根据传言\x01",
            "目标是传说中的古代龙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "以新型引擎的处女秀来说，\x01",
            "算是个完美的对手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1011F嘿，这么有信心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "当然，为了这一天的到来\x01",
            "我不断地进行了各种的调整呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "中央工房的设计者预定\x01",
            "今天也要来记录数据。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "难得有个这么盛大的舞台。\x01",
            "就让『埃尔赛尤』\x01",
            "尽情地发挥它的力量吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A73)
    Jump("loc_112B")

    label("loc_109E")


    ChrTalk(    #50
        0xFE,
        (
            "此次的作战目标\x01",
            "是捕获古代龙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "以新型引擎的处女秀来说，\x01",
            "算得上是个完美的对手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "『埃尔赛尤』应该也能\x01",
            "尽情地发挥它的力量吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112B")

    TalkEnd(0xFE)
    Return()

    # Function_4_BFE end

    def Function_5_112F(): pass

    label("Function_5_112F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BB")

    ChrTalk(    #53
        0xFE,
        "脱落的舷外支架啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "居然决定要用榴弹炮\x01",
            "进行牵引回收了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "据说是穆拉少校的提议，\x01",
            "的确很像陆军国家的想法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_11BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1243")

    ChrTalk(    #56
        0xFE,
        "脱落的舷外支架啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "居然决定要用榴弹炮\x01",
            "进行牵引回收了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "好像是穆拉少校的提议，\x01",
            "的确很像陆军国家的想法呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1286")

    label("loc_1243")


    ChrTalk(    #59
        0xFE,
        (
            "居然将宝贵的榴弹炮\x01",
            "当成拖拉机用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "这点子我们可想不出来。\x02",
    )

    CloseMessageWindow()

    label("loc_1286")

    TalkEnd(0xFE)
    Return()

    # Function_5_112F end

    def Function_6_128A(): pass

    label("Function_6_128A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1461")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132B")

    ChrTalk(    #61
        0xFE,
        (
            "据说要在脱落的左舷部系上锁链\x01",
            "然后再用榴弹炮进行牵引拖曳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "真是粗暴的做法，\x01",
            "不过也没有其他办法了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "无论如何要尝试一下。\x02",
    )

    CloseMessageWindow()
    Jump("loc_145E")

    label("loc_132B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E4")

    ChrTalk(    #64
        0xFE,
        (
            "据说要在脱落的左舷部系上锁链\x01",
            "然后用榴弹炮牵引拖曳……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "真是粗暴的做法，\x01",
            "不过确实只有这样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "结社那些家伙的动向也很让人在意，\x01",
            "所以必须要尽快完成修复才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_145E")

    label("loc_13E4")


    ChrTalk(    #67
        0xFE,
        (
            "结社那些家伙的动向也很让人在意，\x01",
            "所以必须要尽快完成修复才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "真是粗暴的做法，\x01",
            "但只要是有效的手段就必须尝试。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145E")

    Jump("loc_16B6")

    label("loc_1461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_14C9")

    ChrTalk(    #69
        0xFE,
        (
            "多亏有了作业专用的通道，\x01",
            "工作进展容易多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "我想今后修复工程\x01",
            "也会因此而更为迅速哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B6")

    label("loc_14C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_15AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1559")

    ChrTalk(    #71
        0xFE,
        (
            "听说要在舰外开辟\x01",
            "作业专用的通道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "我们正在寻找\x01",
            "有没有什么合适的材料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "拆掉集装箱\x01",
            "拿铁板来用也是一个办法。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_15A9")

    label("loc_1559")


    ChrTalk(    #74
        0xFE,
        (
            "我在为作业专用的通道\x01",
            "寻找材料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "不过，万不得已时\x01",
            "就只能拆掉集装箱了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A9")

    Jump("loc_16B6")

    label("loc_15AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_16B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1656")

    ChrTalk(    #76
        0xFE,
        (
            "在王都政变二次起义中\x01",
            "这里的导力炮也受到袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "虽然全部损坏了，\x01",
            "但幸好马上进行了补充。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "如果没有这个东西，\x01",
            "我们降落之后就等于手无寸铁。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_16B6")

    label("loc_1656")


    ChrTalk(    #79
        0xFE,
        (
            "在王都政变二次起义中\x01",
            "这里的导力炮也受到袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "虽然全部损坏了，\x01",
            "但幸好马上进行了补充。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B6")

    TalkEnd(0xFE)
    Return()

    # Function_6_128A end

    def Function_7_16BA(): pass

    label("Function_7_16BA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16DF")
    Call(0, 23)
    Call(0, 24)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_16DF")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF8, 900, 0, -5260, 90)
    SetChrPos(0xF9, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E8")
    OP_A2(0x1E02)

    ChrTalk(    #81
        0x8,
        "呀，来了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18EE")

    ChrTalk(    #82
        0x101,
        "#1004F#6P啊，菲小姐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x107,
        (
            "#560F#6P您怎么会\x01",
            "在埃尔赛尤号上啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "我是和拉赛尔老爷子\x01",
            "一起搭上这艘船的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "听说维修人员的人手\x01",
            "似乎不太够的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x107,
        (
            "#064F#6P不过，我记得这里\x01",
            "应该有常驻的维修员吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "不，好像是为了\x01",
            "舰艇维修以外的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "我想该不会是来帮忙完成\x01",
            "老爷子的新发明吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x107,
        (
            "#067F#6P嗯。\x01",
            "是有这个可能呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1999")

    label("loc_18EE")


    ChrTalk(    #90
        0x101,
        (
            "#1004F#6P啊，菲小姐？\x02\x03",

            "你怎么会在\x01",
            "埃尔赛尤号上啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "我是和拉赛尔老爷子\x01",
            "一起搭上这艘船的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "听说维修人员的人手\x01",
            "似乎不太够的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1015F#6P哦～是这样啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1999")


    ChrTalk(    #94
        0x8,
        (
            "嗯，反正现在有空\x01",
            "就到船上来帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "那么……\x01",
            "要马上搭乘升降机吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A1E")

    label("loc_19E8")


    ChrTalk(    #96
        0xFE,
        "呀，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "要下降到『翡翠之塔』的前方吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1A1E")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【搭乘升降机】\x01",      # 0
            "【还有点事】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB4")

    ChrTalk(    #98
        0xFE,
        (
            "明白了。\x01",
            "需要时叫我一声哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_1AB4")


    ChrTalk(    #99
        0x8,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "那么请立刻\x01",
            "站到升降机上吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1006F#6P好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2029, 0, -710, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -600, -100, -600, 180)
    SetChrPos(0x102, 600, -100, -600, 180)
    SetChrPos(0xF8, -600, -100, 600, 180)
    SetChrPos(0xF9, 600, -100, 600, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #102
        0xFE,
        "#2P现在要将你们放下去了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "#2P虽然这个应该很平稳\x01",
            "不过你们还是要小心，不要掉下去。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    Sleep(1000)
    OP_6F(0x5, 0)
    OP_70(0x5, 0xA)
    OP_22(0xF7, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #104
        0x101,
        "#1004F#5P哇……\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x100000)
    OP_22(0x68, 0x0, 0x64)
    OP_6F(0x5, 10)
    OP_70(0x5, 0x3C)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_16BA end

    def Function_8_1C65(): pass

    label("Function_8_1C65")

    EventBegin(0x0)
    OP_6D(0, -250, 0, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -620, -4000, -820, 180)
    SetChrPos(0x102, 750, -4000, -780, 180)
    SetChrPos(0xF8, -700, -4000, 280, 180)
    SetChrPos(0xF9, 600, -4000, 290, 180)
    ClearMapFlags(0x100000)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_73(0x5)
    OP_23(0x68)
    OP_22(0xF7, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(70, 0, -3620, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 70, 0, -3620, 180)
    SetChrPos(0x1, 70, 0, -3620, 180)
    SetChrPos(0x2, 70, 0, -3620, 180)
    SetChrPos(0x3, 70, 0, -3620, 180)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_8_1C65 end

    def Function_9_1DA4(): pass

    label("Function_9_1DA4")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF8, 900, 0, -5260, 90)
    SetChrPos(0xF9, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #105
        0x8,
        "呀，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        "要下降到『翡翠之塔』的前方吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【搭乘升降机】\x01",      # 0
            "【还有点事】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F09")

    ChrTalk(    #107
        0x8,
        (
            "明白了。\x01",
            "需要时叫我一声哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_1F09")


    ChrTalk(    #108
        0x8,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        (
            "那么请立刻\x01",
            "站到升降机上吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/R0303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1DA4 end

    def Function_10_1F58(): pass

    label("Function_10_1F58")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F7D")
    Call(0, 23)
    Call(0, 25)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_1F7D")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(500)

    ChrTalk(    #110
        0xFE,
        "呀，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "要下降到『红莲之塔』的前方吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【搭乘升降机】\x01",      # 0
            "【还有点事】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20E0")

    ChrTalk(    #112
        0xFE,
        (
            "明白了。\x01",
            "需要时叫我一声哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_20E0")


    ChrTalk(    #113
        0xFE,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "那么请立刻\x01",
            "站到升降机上吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1F58 end

    def Function_11_212F(): pass

    label("Function_11_212F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2154")
    Call(0, 23)
    Call(0, 25)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2154")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #115
        0xFE,
        "呀，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "要下降到『红莲之塔』的前方吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【搭乘升降机】\x01",      # 0
            "【还有点事】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B7")

    ChrTalk(    #117
        0xFE,
        (
            "明白了。\x01",
            "需要时叫我一声哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_22B7")


    ChrTalk(    #118
        0xFE,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "那么请立刻\x01",
            "站到升降机上吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R3104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_212F end

    def Function_12_2306(): pass

    label("Function_12_2306")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_232B")
    Call(0, 23)
    Call(0, 26)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_232B")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #120
        0x8,
        "呀，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        "要下降到『绀碧之塔』的前方吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【搭乘升降机】\x01",      # 0
            "【还有点事】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_248E")

    ChrTalk(    #122
        0xFE,
        (
            "明白了。\x01",
            "需要时叫我一声哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_248E")


    ChrTalk(    #123
        0xFE,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "那么请立刻\x01",
            "站到升降机上吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2306 end

    def Function_13_24DD(): pass

    label("Function_13_24DD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2502")
    Call(0, 23)
    Call(0, 26)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2502")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #125
        0x8,
        "呀，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        "要下降到『绀碧之塔』的前方吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【搭乘升降机】\x01",      # 0
            "【还有点事】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2665")

    ChrTalk(    #127
        0xFE,
        (
            "明白了。\x01",
            "需要时叫我一声哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_2665")


    ChrTalk(    #128
        0xFE,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "那么请立刻\x01",
            "站到升降机上吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_24DD end

    def Function_14_26B4(): pass

    label("Function_14_26B4")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26D9")
    Call(0, 23)
    Call(0, 24)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_26D9")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #130
        0x8,
        "终于到最后的塔了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        "要下降到『琥珀之塔』的前方吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【搭乘升降机】\x01",      # 0
            "【还有点事】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2842")

    ChrTalk(    #132
        0xFE,
        (
            "明白了。\x01",
            "需要时叫我一声哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_2842")


    ChrTalk(    #133
        0xFE,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "那么请立刻\x01",
            "站到升降机上吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_26B4 end

    def Function_15_2891(): pass

    label("Function_15_2891")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28B6")
    Call(0, 23)
    Call(0, 24)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_28B6")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #135
        0x8,
        "终于到最后的塔了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        "要下降到『琥珀之塔』的前方吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【搭乘升降机】\x01",      # 0
            "【还有点事】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1F")

    ChrTalk(    #137
        0xFE,
        (
            "明白了。\x01",
            "需要时叫我一声哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_2A1F")


    ChrTalk(    #138
        0xFE,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "那么请立刻\x01",
            "站到升降机上吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_2891 end

    def Function_16_2A6E(): pass

    label("Function_16_2A6E")

    Sleep(300)
    Fade(500)
    OP_6D(2029, 0, -710, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -600, -100, -600, 180)
    SetChrPos(0x102, 600, -100, -600, 180)
    SetChrPos(0xF8, -600, -100, 600, 180)
    SetChrPos(0xF9, 600, -100, 600, 180)
    OP_0D()
    Sleep(300)
    OP_8C(0x8, 90, 400)
    Sleep(1000)
    OP_6F(0x5, 0)
    OP_70(0x5, 0xA)
    OP_22(0xF7, 0x0, 0x64)
    Sleep(1000)
    SetMapFlags(0x100000)
    OP_22(0x68, 0x0, 0x64)
    OP_6F(0x5, 10)
    OP_70(0x5, 0x3C)
    Sleep(1000)
    Return()

    # Function_16_2A6E end

    def Function_17_2B41(): pass

    label("Function_17_2B41")

    OP_8E(0xFE, 0xFFFFFDDA, 0xFFFFFF06, 0xFFFFFDDA, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_2B41 end

    def Function_18_2B5D(): pass

    label("Function_18_2B5D")

    OP_8E(0xFE, 0xFFFFFDDA, 0xFFFFFF06, 0x226, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_2B5D end

    def Function_19_2B79(): pass

    label("Function_19_2B79")

    OP_8E(0xFE, 0x226, 0xFFFFFF06, 0xFFFFFDDA, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_2B79 end

    def Function_20_2B95(): pass

    label("Function_20_2B95")

    OP_8E(0xFE, 0x226, 0x0, 0x11B2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x226, 0xFFFFFF06, 0x226, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_20_2B95 end

    def Function_21_2BC5(): pass

    label("Function_21_2BC5")

    OP_8E(0xFE, 0x8B6, 0x0, 0x18D8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_21_2BC5 end

    def Function_22_2BE1(): pass

    label("Function_22_2BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2C19")
    EventBegin(0x2)
    FadeToDark(500, 0, -1)
    OP_8C(0x0, 180, 0)
    OP_91(0x0, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
    OP_0D()
    NewScene("ED6_DT21/C5900   ._SN", 102, 0, 0)
    IdleLoop()

    label("loc_2C19")

    Return()

    # Function_22_2BE1 end

    def Function_23_2C1A(): pass

    label("Function_23_2C1A")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C94"),
        (1, "loc_2C9A"),
        (SWITCH_DEFAULT, "loc_2CA0"),
    )


    label("loc_2C94")

    OP_A2(0x1200)
    Jump("loc_2CA0")

    label("loc_2C9A")

    OP_A2(0x1201)
    Jump("loc_2CA0")

    label("loc_2CA0")

    Return()

    # Function_23_2C1A end

    def Function_24_2CA1(): pass

    label("Function_24_2CA1")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_24_2CA1 end

    def Function_25_2D30(): pass

    label("Function_25_2D30")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_25_2D30 end

    def Function_26_2DBD(): pass

    label("Function_26_2DBD")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_26_2DBD end

    def Function_27_2E4A(): pass

    label("Function_27_2E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB1")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #140
        "\x07\x05门紧紧地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2EB1")

    Return()

    # Function_27_2E4A end

    SaveToFile()

Try(main)
