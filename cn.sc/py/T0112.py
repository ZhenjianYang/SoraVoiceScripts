from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0112   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0112.x',
        MapIndex            = 11,
        MapDefaultBGM       = "ed60084",
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
        '鲁克',                                 # 9
        '玛茜婆婆',                             # 10
        '帕特',                                 # 11
        '雷特拉',                               # 12
        '赛拉',                                 # 13
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
        'ED6_DT26/CH20330 ._CH',             # 00
        'ED6_DT07/CH01110 ._CH',             # 01
        'ED6_DT07/CH01060 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT26/CH20330P._CP',             # 00
        'ED6_DT07/CH01110P._CP',             # 01
        'ED6_DT07/CH01060P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 93320,
        Z                   = 0,
        Y                   = 162900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 88100,
        Z                   = 0,
        Y                   = 162410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_1EB",          # 01, 1
        "Function_2_1FA",          # 02, 2
        "Function_3_377",          # 03, 3
        "Function_4_465",          # 04, 4
        "Function_5_4BB",          # 05, 5
        "Function_6_5B3",          # 06, 6
        "Function_7_696",          # 07, 7
        "Function_8_791",          # 08, 8
    )


    def Function_0_172(): pass

    label("Function_0_172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1D3")
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 55200, 100, 159950, 180)
    SetChrPos(0x9, 55120, 0, 161430, 180)
    SetChrPos(0xA, 56170, 0, 161420, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0x8, 4)

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1EA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 7)

    label("loc_1EA")

    Return()

    # Function_0_172 end

    def Function_1_1EB(): pass

    label("Function_1_1EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1F9")
    OP_6F(0x2, 15)

    label("loc_1F9")

    Return()

    # Function_1_1EB end

    def Function_2_1FA(): pass

    label("Function_2_1FA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_361")

    label("loc_21F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_361")

    label("loc_238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_361")

    label("loc_251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_361")

    label("loc_26A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_361")

    label("loc_283")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_361")

    label("loc_29C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_361")

    label("loc_2B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_361")

    label("loc_2CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_361")

    label("loc_2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_361")

    label("loc_300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_361")

    label("loc_319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_361")

    label("loc_332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_361")

    label("loc_34B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_361")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_376")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_361")

    label("loc_376")

    Return()

    # Function_2_1FA end

    def Function_3_377(): pass

    label("Function_3_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_386")
    Call(0, 8)
    Jump("loc_464")

    label("loc_386")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3E7")

    ChrTalk(    #0
        0xFE,
        (
            "这孩子是个精力用不完的\x01",
            "淘气小鬼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "没事的，到明早一定会\x01",
            "像平时一样醒来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_461")

    label("loc_3E7")


    ChrTalk(    #2
        0xFE,
        (
            "这孩子是个精力用不完的\x01",
            "淘气小鬼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "没事的，到明早一定会\x01",
            "像平时一样醒来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "又会不吃早饭\x01",
            "就飞跑出去的……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_461")

    TalkEnd(0x9)

    label("loc_464")

    Return()

    # Function_3_377 end

    def Function_4_465(): pass

    label("Function_4_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_474")
    Call(0, 8)
    Jump("loc_4BA")

    label("loc_474")

    TalkBegin(0xA)

    ChrTalk(    #5
        0xA,
        (
            "艾丝蒂尔姐姐…\x01",
            "我不会再哭了。\x02\x03",

            "因为我不想让鲁克\x01",
            "看见我哭。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)

    label("loc_4BA")

    Return()

    # Function_4_465 end

    def Function_5_4BB(): pass

    label("Function_5_4BB")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_5AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_52C")

    ChrTalk(    #6
        0xFE,
        (
            "隔壁的鲁克\x01",
            "突然昏倒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "我家帕特也担心得\x01",
            "跑去看他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "希望他别受\x01",
            "什么打击……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF")

    label("loc_52C")


    ChrTalk(    #9
        0xFE,
        (
            "隔壁的鲁克\x01",
            "突然昏倒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "苏醒药也不起作用，\x01",
            "真让人担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "鲁克是我家帕特的\x01",
            "好朋友。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "希望他别受\x01",
            "什么打击……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_5AF")

    TalkEnd(0xB)
    Return()

    # Function_5_4BB end

    def Function_6_5B3(): pass

    label("Function_6_5B3")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_692")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_605")

    ChrTalk(    #13
        0xFE,
        (
            "帕特不肯\x01",
            "离开鲁克。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "没办法，我只能拜托\x01",
            "玛茜婆婆了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_692")

    label("loc_605")


    ChrTalk(    #15
        0xFE,
        (
            "帕特去了隔壁的\x01",
            "阿斯顿家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "他怎么也不肯\x01",
            "离开鲁克……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "没办法，我只能拜托\x01",
            "玛茜婆婆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "我想今天再稍微\x01",
            "让他在那边待会儿。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_692")

    TalkEnd(0xC)
    Return()

    # Function_6_5B3 end

    def Function_7_696(): pass

    label("Function_7_696")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x8, 255)
    OP_6F(0x2, 15)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 55200, 100, 159950, 180)
    SetChrPos(0x9, 55120, 0, 161430, 180)
    SetChrPos(0xA, 56170, 0, 161420, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0x8, 4)
    OP_6D(52310, 0, 164340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(54780, 0, 161440, 3000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0113   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_7_696 end

    def Function_8_791(): pass

    label("Function_8_791")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    Fade(1000)
    SetChrPos(0x101, 56220, 0, 162560, 180)
    SetChrPos(0x103, 55060, 0, 162840, 180)
    SetChrPos(0xF8, 55900, 0, 164050, 180)
    SetChrPos(0xF9, 54700, 0, 164240, 180)
    OP_8C(0x9, 0, 0)
    OP_8C(0xA, 0, 0)
    OP_6D(55170, 0, 162450, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇鲁克和帕特没有重逢】\x01",      # 0
            "【◇鲁克和帕特已经重逢】\x01",      # 1
            "【◇不变更】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8C3"),
        (1, "loc_8C9"),
        (SWITCH_DEFAULT, "loc_8CF"),
    )


    label("loc_8C3")

    OP_A3(0x1883)
    Jump("loc_8CF")

    label("loc_8C9")

    OP_A2(0x1883)
    Jump("loc_8CF")

    label("loc_8CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_964")

    ChrTalk(    #19
        0xA,
        "啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        "#6P哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "#6P这不是布莱特家的\x01",
            "艾丝蒂尔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1025F#2P好久不见。\x01",
            "玛茜婆婆、帕特。\x02\x03",

            "#1003F鲁克……\x01",
            "很麻烦吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EE")

    label("loc_964")


    ChrTalk(    #23
        0xA,
        (
            "啊……\x01",
            "艾丝蒂尔姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        "#6P哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#6P这不是布莱特家的\x01",
            "艾丝蒂尔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1025F#2P那个，晚上好。\x02\x03",

            "#1003F鲁克……\x01",
            "很麻烦吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EE")


    ChrTalk(    #27
        0xA,
        (
            "呜呜，姐姐……\x02\x03",

            "艾丝蒂尔姐姐！！\x02",
        )
    )

    CloseMessageWindow()
    OP_D2(0x260110, 0x260115, 0x5)
    SetChrFlags(0xA, 0x40)
    OP_8F(0xA, 0xDBCE, 0x0, 0x27A38, 0xFA0, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0xA, 0x80)
    OP_91(0x101, 0x0, 0x0, 0xC8, 0xFA0, 0x0)

    def lambda_A65():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A65)
    Sleep(50)

    def lambda_A78():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A78)
    Sleep(50)

    def lambda_A8B():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A8B)
    Sleep(400)

    ChrTalk(    #28
        0x101,
        (
            "#1004F#2P哇哇……\x01",
            "怎么了？帕特？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        "#6P也难怪……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "#6P是这孩子发现鲁克\x01",
            "倒在地上的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1003F#2P这样啊……\x02\x03",

            "#1025F帕特……辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        "#6P呜……呜……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)
    Sleep(500)

    ChrTalk(    #33
        0x103,
        (
            "#022F玛茜婆婆，\x01",
            "您孙子的情况怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#6P嗯，现在\x01",
            "睡得很熟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        (
            "#6P没事，不用担心，\x01",
            "到早上一定会起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#6P因为他是个只有精力用不完的\x01",
            "淘气小鬼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "#6P怎么可能从此\x01",
            "一睡不起呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        "#522F玛茜婆婆……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1010F#2P……………………………\x02\x03",

            "#1002F……我说，帕特，\x02\x03",

            "能不能跟我说说\x01",
            "鲁克睡着时的样子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        "#6P……咦………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 400)

    ChrTalk(    #41
        0x101,
        (
            "#1002F#2P我们受市长先生的委托\x01",
            "来调查此次的事件。\x02\x03",

            "如果帕特告诉我们线索，\x01",
            "我们就会离案件解决更近一步了。\x02\x03",

            "所以……拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "#6P姐姐……\x02\x03",

            "……嗯………\x01",
            "我……会详细说的。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0xA, 0x80)
    OP_0D()
    OP_8F(0xA, 0xDB6A, 0x0, 0x278D0, 0x3E8, 0x0)
    ClearChrFlags(0xA, 0x40)

    def lambda_D90():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D90)
    Sleep(50)

    def lambda_DA3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_DA3)
    Sleep(50)

    def lambda_DB6():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_DB6)
    Sleep(400)

    ChrTalk(    #43
        0x101,
        (
            "#1025F#2P谢谢你，帕特。\x02\x03",

            "#1002F那么，鲁克是在\x01",
            "何时何地睡着的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        (
            "#6P啊，嗯……\x02\x03",

            "我是在钟楼\x01",
            "发现鲁克的。\x02\x03",

            "时间是……\x01",
            "５点过一点点。\x02\x03",

            "那时，我们在雾中\x01",
            "玩捉迷藏……\x02\x03",

            "我扮鬼，正在找\x01",
            "躲着的鲁克。\x02\x03",

            "可当我好不容易找到他时，\x01",
            "他却睡着了……\x02\x03",

            "当我没办法只能把他叫醒的时候，\x01",
            "他却醒不过来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1007F#2P是吗……\x02\x03",

            "#1015F那么是谁把鲁克\x01",
            "送来这里的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "#6P啊，嗯，\x01",
            "是看守钟楼的潘杜爷爷。\x02\x03",

            "正在我感到为难时，\x01",
            "他走了上来。\x02\x03",

            "他是来查看钟有没有\x01",
            "因为雾而出故障的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1011F#2P是这样啊……\x01",
            "的确是潘杜爷爷的作风。\x02\x03",

            "#1006F嗯，大体情况我了解了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#020F……那么，帕特，\x02\x03",

            "捉迷藏时，\x01",
            "有没有发生什么怪事？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #49
        0xA,
        "#6P怪事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#020F比如见到陌生人或者\x01",
            "听到怪异的声音？\x02\x03",

            "什么都可以。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#6P唔……\x02\x03",

            "除了纯白色的雾之外\x01",
            "其它不记得什么了……\x02\x03",

            "还有就是飞船坪里没有人，\x01",
            "稍微有点可怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        "#524F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1015F#2P看来没什么\x01",
            "可疑的事发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        (
            "#026F嗯……是啊。\x02\x03",

            "#020F谢谢你们，\x01",
            "给我们提供了很好的参考。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "#6P是吗……\x01",
            "那就太好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(500)

    ChrTalk(    #56
        0xA,
        (
            "#6P艾丝蒂尔姐姐……\x01",
            "鲁克，会没事的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1006F#2P嗯……当然了。\x02\x03",

            "帕特你也\x01",
            "别再哭鼻子了。\x02\x03",

            "不然鲁克醒过来时\x01",
            "可会笑话你的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "#6P嗯、嗯……\x02\x03",

            "是啊。\x01",
            "我不会再哭了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(53810, 0, 164450, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 53810, 0, 164450, 0)
    SetChrPos(0x103, 53810, 0, 164450, 0)
    SetChrPos(0xF8, 53810, 0, 164450, 0)
    SetChrPos(0xF9, 53810, 0, 164450, 0)
    SetChrPos(0xA, 56170, 0, 161420, 180)
    OP_8C(0x9, 180, 0)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_A2(0x1816)
    OP_28(0x90, 0x2, 0x20)
    OP_28(0x90, 0x1, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FF")
    OP_28(0x90, 0x1, 0x200)
    Jump("loc_12FF")

    label("loc_12FF")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_791 end

    SaveToFile()

Try(main)
