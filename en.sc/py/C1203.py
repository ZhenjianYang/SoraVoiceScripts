from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Renne',                                # 9
        'Gospel',                               # 10
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
        "Function_4_530",          # 04, 4
        "Function_5_1273",         # 05, 5
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
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Leave Alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_275"),
        (1, "loc_4C5"),
        (SWITCH_DEFAULT, "loc_52D"),
    )


    label("loc_275")

    Battle(0x93, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_296"),
        (2, "loc_445"),
        (1, "loc_4BD"),
        (SWITCH_DEFAULT, "loc_4C2"),
    )


    label("loc_296")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xA, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Set as exterminated the wanted monsters in Nebel Valley and at Krone Pass.\x01",      # 0
            "No change\x01",                                                                       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_339"),
        (SWITCH_DEFAULT, "loc_34E"),
    )


    label("loc_339")

    OP_A2(0x1A0E)
    OP_A2(0x1A10)
    OP_28(0xB1, 0x1, 0x1)
    OP_28(0xB2, 0x1, 0x1)
    Jump("loc_34E")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_360")
    Call(0, 4)
    Jump("loc_442")

    label("loc_360")

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
        "\x07\x05Exterminated monster at Amberl Tower!\x02",
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

    label("loc_442")

    Jump("loc_4C2")

    label("loc_445")

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
    Jump("loc_4C2")

    label("loc_4BD")

    OP_B4(0x0)
    Jump("loc_4C2")

    label("loc_4C2")

    Jump("loc_52D")

    label("loc_4C5")

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
    Jump("loc_52D")

    label("loc_52D")

    EventEnd(0x0)
    Return()

    # Function_3_1F9 end

    def Function_4_530(): pass

    label("Function_4_530")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_543")
    Call(0, 5)

    label("loc_543")

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
            "#1007FPhew! That's the last one.\x02\x03",

            "#1002FStill, though.\x01",
            "Didn't they seem kind of odd?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x18\x07\x05What seemed odd about the monsters?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "The Monsters Were Strong\x01",        # 0
            "The Monsters Were Afraid\x01",        # 1
            "The Monsters Were Agitated\x01",      # 2
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
        (0, "loc_707"),
        (1, "loc_99F"),
        (2, "loc_BF2"),
        (SWITCH_DEFAULT, "loc_E45"),
    )


    label("loc_707")

    OP_2B(0x93, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A3")

    ChrTalk(    #4
        0x108,
        (
            "#072FIt was a challenge, but...\x01",
            "the monsters' behavior was odd, as well.\x02\x03",

            "Some were ready to kill us,\x01",
            "some were ready to flee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_996")

    label("loc_7A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_849")

    ChrTalk(    #5
        0x103,
        (
            "#022FThat's definitely true, but...\x01",
            "it also felt like they were acting\x01",
            "very strangely.\x02\x03",

            "Some were bizarrely ferocious,\x01",
            "others were panicking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_996")

    label("loc_849")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F1")

    ChrTalk(    #6
        0x104,
        (
            "#032FPerhaps. But there seemed to be\x01",
            "more to it.\x02\x03",

            "Some bared their fangs at us in fury,\x01",
            "others were ready to flee from us like\x01",
            "scared children...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_996")

    label("loc_8F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_996")

    ChrTalk(    #7
        0x105,
        (
            "#043FThey were certainly powerful,\x01",
            "but their behavior... It was so odd.\x02\x03",

            "Some of them were blind with fury,\x01",
            "but others were panicked and fearful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_996")

    OP_28(0x93, 0x1, 0x400)
    Jump("loc_E45")

    label("loc_99F")

    OP_2B(0x93, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1C")

    ChrTalk(    #8
        0x108,
        (
            "#072FYes, the monsters' behavior was odd.\x02\x03",

            "Some were ready to kill us,\x01",
            "some were ready to flee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE9")

    label("loc_A1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA0")

    ChrTalk(    #9
        0x103,
        (
            "#022FYes, all of the monsters were acting\x01",
            "strangely.\x02\x03",

            "Some were bizarrely ferocious,\x01",
            "others were panicking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE9")

    label("loc_AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B55")

    ChrTalk(    #10
        0x104,
        (
            "#032FHmm. Yes, their behavior was,\x01",
            "unusual, to say the least.\x02\x03",

            "Some bared their fangs at us in fury,\x01",
            "others were ready to flee from us like\x01",
            "scared children...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE9")

    label("loc_B55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE9")

    ChrTalk(    #11
        0x105,
        (
            "#042FYes, the behavior of the monsters was...\x01",
            "bizarre.\x02\x03",

            "Some of them were blind with fury,\x01",
            "but others were panicked and fearful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE9")

    OP_28(0x93, 0x1, 0x1000)
    Jump("loc_E45")

    label("loc_BF2")

    OP_2B(0x93, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6F")

    ChrTalk(    #12
        0x108,
        (
            "#072FYes, the monsters' behavior was odd.\x02\x03",

            "Some were ready to kill us,\x01",
            "some were ready to flee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C")

    label("loc_C6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF3")

    ChrTalk(    #13
        0x103,
        (
            "#022FYes, all of the monsters were acting strangely.\x02\x03",

            "Some were bizarrely ferocious,\x01",
            "others were panicking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C")

    label("loc_CF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA8")

    ChrTalk(    #14
        0x104,
        (
            "#032FHmm. Yes, their behavior was,\x01",
            "to say the least, unusual.\x02\x03",

            "Some bared their fangs at us in fury,\x01",
            "others were ready to flee from us like\x01",
            "scared children...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C")

    label("loc_DA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E3C")

    ChrTalk(    #15
        0x105,
        (
            "#042FYes, the behavior of the monsters was...\x01",
            "bizarre.\x02\x03",

            "Some of them were blind with fury,\x01",
            "but others were panicked and fearful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3C")

    OP_28(0x93, 0x1, 0x800)
    Jump("loc_E45")

    label("loc_E45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E96")

    ChrTalk(    #16
        0x107,
        (
            "#065FI kinda noticed that too.\x02\x03",

            "#561FIt was kinda scary...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA5")

    label("loc_E96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE4")

    ChrTalk(    #17
        0x105,
        (
            "#043FI also noticed that.\x02\x03",

            "I wonder what it could mean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA5")

    label("loc_EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F50")

    ChrTalk(    #18
        0x104,
        (
            "#032FI, too, could not help but notice\x01",
            "their confusion.\x02\x03",

            "I wish I knew what it meant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA5")

    label("loc_F50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA5")

    ChrTalk(    #19
        0x103,
        (
            "#026FI got the same impression.\x02\x03",

            "#522FMmmm... What could it mean?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA5")


    ChrTalk(    #20
        0x106,
        "#057F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1004FAgate? Something up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x106,
        (
            "#555FEh...\x02\x03",

            "Just thinkin' this might be a warning\x01",
            "about somethin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1020FA warning... You mean to something\x01",
            "Ouroboros is doing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "#552FI can't say for sure, but...somethin'\x01",
            "like this has happened before.\x02\x03",

            "Day after day, the monsters were all\x01",
            "riled up.\x02\x03",

            "And then, bam, right after that...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1004FRight after...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1143")

    ChrTalk(    #26
        0x107,
        "#063FAgate...?\x02",
    )

    CloseMessageWindow()

    label("loc_1143")


    ChrTalk(    #27
        0x106,
        (
            "#053FEnough 'bout that.\x02\x03",

            "#057FPoint is, animals have better instincts\x01",
            "about this sorta stuff than us humans do.\x02\x03",

            "We'd better keep our eyes open for anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1002FYeah...good point.\x02\x03",

            "Back to the guildhouse for us, then,\x01",
            "I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x106,
        "#050FSounds like a plan.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A0F)
    OP_28(0xB3, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x10)
    OP_28(0x93, 0x1, 0x20)
    OP_28(0x93, 0x1, 0x40)
    OP_28(0x93, 0x1, 0x2000)
    Return()

    # Function_4_530 end

    def Function_5_1273(): pass

    label("Function_5_1273")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1329"),
        (1, "loc_132F"),
        (SWITCH_DEFAULT, "loc_1335"),
    )


    label("loc_1329")

    OP_A2(0x1200)
    Jump("loc_1335")

    label("loc_132F")

    OP_A2(0x1201)
    Jump("loc_1335")

    label("loc_1335")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_5_1273 end

    SaveToFile()

Try(main)
