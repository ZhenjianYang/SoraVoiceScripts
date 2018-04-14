from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1203   ._SN',
        MapName             = 'Bose',
        Location            = 'C1203.x',
        MapIndex            = 51,
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
        '歼灭天使玲',                           # 9
        '假福音',                               # 10
        '',                                     # 11
        '',                                     # 12
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
        'ED6_DT27/CH03510 ._CH',             # 00
        'ED6_DT29/CH12450 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT29/CH12140 ._CH',             # 03
        'ED6_DT29/CH12141 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03510P._CP',             # 00
        'ED6_DT29/CH12450P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT29/CH12140P._CP',             # 03
        'ED6_DT29/CH12141P._CP',             # 04
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 11390,
        Z                   = 250,
        Y                   = 5670,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 8790,
        Z                   = 250,
        Y                   = 12470,
        Unknown_0C          = 270,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x8E,
        Unknown_18          = 8450,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 11390,
        Y                   = 250,
        Z                   = 5670,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_16E",          # 00, 0
        "Function_1_189",          # 01, 1
        "Function_2_1E3",          # 02, 2
        "Function_3_1F9",          # 03, 3
        "Function_4_4F9",          # 04, 4
        "Function_5_F2A",          # 05, 5
    )


    def Function_0_16E(): pass

    label("Function_0_16E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 2)), scpexpr(EXPR_END)), "loc_17A")
    SetChrFlags(0xB, 0x80)

    label("loc_17A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188")
    OP_B5(0x0)

    label("loc_188")

    Return()

    # Function_0_16E end

    def Function_1_189(): pass

    label("Function_1_189")

    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C6")
    ClearChrFlags(0xA, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_1C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_72(0x0, 0x4)

    label("loc_1DD")

    OP_22(0x1C3, 0x1, 0x64)
    Return()

    # Function_1_189 end

    def Function_2_1E3(): pass

    label("Function_2_1E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1E3")

    label("loc_1F8")

    Return()

    # Function_2_1E3 end

    def Function_3_1F9(): pass

    label("Function_3_1F9")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05巨大的魔兽正四处徘徊。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_260"),
        (1, "loc_48E"),
        (SWITCH_DEFAULT, "loc_4F6"),
    )


    label("loc_260")

    Battle(0x93, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_281"),
        (2, "loc_40E"),
        (1, "loc_486"),
        (SWITCH_DEFAULT, "loc_48B"),
    )


    label("loc_281")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xA, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【◇消灭了古罗尼峰和迷雾峡谷的通缉魔兽】\x01",      # 0
            "【◇什么也没有变更】\x01",                          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30D"),
        (SWITCH_DEFAULT, "loc_322"),
    )


    label("loc_30D")

    OP_A2(0x1A0E)
    OP_A2(0x1A10)
    OP_28(0xB1, 0x1, 0x1)
    OP_28(0xB2, 0x1, 0x1)
    Jump("loc_322")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_334")
    Call(0, 4)
    Jump("loc_40B")

    label("loc_334")

    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, 11390, 250, 5670, 45)
    SetChrPos(0x1, 11390, 250, 5670, 45)
    SetChrPos(0x2, 11390, 250, 5670, 45)
    SetChrPos(0x3, 11390, 250, 5670, 45)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05消灭了琥珀之塔的通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1A0F)
    OP_28(0xB3, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x10)
    OP_28(0x93, 0x1, 0x20)
    OP_28(0x93, 0x1, 0x40)
    Sleep(400)

    label("loc_40B")

    Jump("loc_48B")

    label("loc_40E")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, 7940, 250, 1990, 45)
    SetChrPos(0x1, 7940, 250, 1990, 45)
    SetChrPos(0x2, 7940, 250, 1990, 45)
    SetChrPos(0x3, 7940, 250, 1990, 45)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_48B")

    label("loc_486")

    OP_B4(0x0)
    Jump("loc_48B")

    label("loc_48B")

    Jump("loc_4F6")

    label("loc_48E")

    Fade(500)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, 7940, 250, 1990, 45)
    SetChrPos(0x1, 7940, 250, 1990, 45)
    SetChrPos(0x2, 7940, 250, 1990, 45)
    SetChrPos(0x3, 7940, 250, 1990, 45)
    OP_69(0x0, 0x0)
    OP_0D()
    Jump("loc_4F6")

    label("loc_4F6")

    EventEnd(0x0)
    Return()

    # Function_3_1F9 end

    def Function_4_4F9(): pass

    label("Function_4_4F9")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50C")
    Call(0, 5)

    label("loc_50C")

    OP_6D(11780, 250, 5320, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 12050, 250, 4660, 270)
    SetChrPos(0x106, 11110, 250, 5750, 180)
    SetChrPos(0xF8, 10510, 250, 3060, 0)
    SetChrPos(0xF9, 9550, 250, 4240, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #2
        0x101,
        (
            "#1007F哈～总算是解决了啊。\x02\x03",

            "#1002F不过……\x01",
            "这些魔兽的样子似乎很奇怪啊？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x18\x07\x05是哪里和平时不同了呢？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【魔兽变强了】\x01",        # 0
            "【魔兽变胆怯了】\x01",      # 1
            "【魔兽非常兴奋】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_69A"),
        (1, "loc_873"),
        (2, "loc_A1A"),
        (SWITCH_DEFAULT, "loc_BC7"),
    )


    label("loc_69A")

    OP_2B(0x93, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70F")

    ChrTalk(    #4
        0x108,
        (
            "#072F那也没错……\x01",
            "不过更明显的是它们的性情变了。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A")

    label("loc_70F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_785")

    ChrTalk(    #5
        0x103,
        (
            "#022F那也说的没错……\x01",
            "不过更明显的是它们的性情变了哦。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A")

    label("loc_785")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FD")

    ChrTalk(    #6
        0x104,
        (
            "#032F嗯，那也说的不错，\x01",
            "不过更明显的是它们的性情变了哦。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A")

    label("loc_7FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86A")

    ChrTalk(    #7
        0x105,
        (
            "#043F那样说也对，\x01",
            "不过更明显的是它们的性情变了。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86A")

    OP_28(0x93, 0x1, 0x400)
    Jump("loc_BC7")

    label("loc_873")

    OP_2B(0x93, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E0")

    ChrTalk(    #8
        0x108,
        (
            "#072F啊啊～每一处的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11")

    label("loc_8E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_946")

    ChrTalk(    #9
        0x103,
        (
            "#022F哎～每一处的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11")

    label("loc_946")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AE")

    ChrTalk(    #10
        0x104,
        (
            "#032F嗯，不管是什么魔兽\x01",
            "都好像很奇怪啊。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11")

    label("loc_9AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A11")

    ChrTalk(    #11
        0x105,
        (
            "#042F是啊，不管是什么魔兽\x01",
            "都很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A11")

    OP_28(0x93, 0x1, 0x1000)
    Jump("loc_BC7")

    label("loc_A1A")

    OP_2B(0x93, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A89")

    ChrTalk(    #12
        0x108,
        (
            "#072F啊啊～不管是什么魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBE")

    label("loc_A89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF1")

    ChrTalk(    #13
        0x103,
        (
            "#022F哎～不管是什么魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBE")

    label("loc_AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B59")

    ChrTalk(    #14
        0x104,
        (
            "#032F嗯，不管是什么魔兽\x01",
            "都好像很奇怪啊。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBE")

    label("loc_B59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBE")

    ChrTalk(    #15
        0x105,
        (
            "#042F是啊，不管是什么魔兽\x01",
            "也都很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBE")

    OP_28(0x93, 0x1, 0x800)
    Jump("loc_BC7")

    label("loc_BC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0F")

    ChrTalk(    #16
        0x107,
        (
            "#065F我、我也\x01",
            "有那种感觉。\x02\x03",

            "#561F好、好可怕啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4")

    label("loc_C0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C56")

    ChrTalk(    #17
        0x105,
        (
            "#043F我也……\x01",
            "有那种感觉啊。\x02\x03",

            "究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4")

    label("loc_C56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9D")

    ChrTalk(    #18
        0x104,
        (
            "#032F我也有\x01",
            "同样的感觉呢。\x02\x03",

            "嗯，到底是为什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4")

    label("loc_C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE4")

    ChrTalk(    #19
        0x103,
        (
            "#026F我也有同感啊。\x02\x03",

            "#522F嗯……\x01",
            "究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE4")


    ChrTalk(    #20
        0x106,
        "#057F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1004F嗯？　怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x106,
        (
            "#555F啊，没什么……\x02\x03",

            "或许这是\x01",
            "某种前兆也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1020F前兆……\x01",
            "难道是『结社』！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "#552F那就不知道了……\x01",
            "不过以前也发生过类似的状况。\x02\x03",

            "魔兽突然就变得\x01",
            "仓惶不安…\x02\x03",

            "之后……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1004F？？？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2E")

    ChrTalk(    #26
        0x107,
        "#063F阿加特哥哥……？\x02",
    )

    CloseMessageWindow()

    label("loc_E2E")


    ChrTalk(    #27
        0x106,
        (
            "#053F算了，目前就这样吧。\x02\x03",

            "#057F不管怎么说，动物的直觉\x01",
            "有时候比人还要更加敏锐。\x02\x03",

            "我们也必须准备应付\x01",
            "随时可能出现的特殊情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1002F嗯……明白了。\x02\x03",

            "那么…\x01",
            "我们暂时先返回协会吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x106,
        "#050F啊啊～就这样办吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A0F)
    OP_28(0xB3, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x10)
    OP_28(0x93, 0x1, 0x20)
    OP_28(0x93, 0x1, 0x40)
    OP_28(0x93, 0x1, 0x2000)
    Return()

    # Function_4_4F9 end

    def Function_5_F2A(): pass

    label("Function_5_F2A")

    FadeToDark(0, 0, -1)
    OP_6D(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0, "loc_FE1"),
        (1, "loc_FE7"),
        (SWITCH_DEFAULT, "loc_FED"),
    )


    label("loc_FE1")

    OP_A2(0x1200)
    Jump("loc_FED")

    label("loc_FE7")

    OP_A2(0x1201)
    Jump("loc_FED")

    label("loc_FED")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_5_F2A end

    SaveToFile()

Try(main)
