from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4230   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4230.x',
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
        'Queen Alicia',                         # 9
        'Duke Dunan',                           # 10
        'Butler Phillip',                       # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Special Ops Soldier',                  # 15
        'Shea',                                 # 16
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
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH00000 ._CH',             # 03
        'ED6_DT07/CH00010 ._CH',             # 04
        'ED6_DT07/CH02010 ._CH',             # 05
        'ED6_DT07/CH02140 ._CH',             # 06
        'ED6_DT07/CH02470 ._CH',             # 07
        'ED6_DT07/CH01330 ._CH',             # 08
        'ED6_DT07/CH00100 ._CH',             # 09
        'ED6_DT07/CH00101 ._CH',             # 0A
        'ED6_DT07/CH00120 ._CH',             # 0B
        'ED6_DT07/CH00121 ._CH',             # 0C
        'ED6_DT07/CH00140 ._CH',             # 0D
        'ED6_DT07/CH00141 ._CH',             # 0E
        'ED6_DT07/CH02540 ._CH',             # 0F
        'ED6_DT07/CH00440 ._CH',             # 10
        'ED6_DT07/CH00441 ._CH',             # 11
        'ED6_DT07/CH00500 ._CH',             # 12
        'ED6_DT07/CH00501 ._CH',             # 13
        'ED6_DT06/CH20042 ._CH',             # 14
        'ED6_DT06/CH20089 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH00000P._CP',             # 03
        'ED6_DT07/CH00010P._CP',             # 04
        'ED6_DT07/CH02010P._CP',             # 05
        'ED6_DT07/CH02140P._CP',             # 06
        'ED6_DT07/CH02470P._CP',             # 07
        'ED6_DT07/CH01330P._CP',             # 08
        'ED6_DT07/CH00100P._CP',             # 09
        'ED6_DT07/CH00101P._CP',             # 0A
        'ED6_DT07/CH00120P._CP',             # 0B
        'ED6_DT07/CH00121P._CP',             # 0C
        'ED6_DT07/CH00140P._CP',             # 0D
        'ED6_DT07/CH00141P._CP',             # 0E
        'ED6_DT07/CH02540P._CP',             # 0F
        'ED6_DT07/CH00440P._CP',             # 10
        'ED6_DT07/CH00441P._CP',             # 11
        'ED6_DT07/CH00500P._CP',             # 12
        'ED6_DT07/CH00501P._CP',             # 13
        'ED6_DT06/CH20042P._CP',             # 14
        'ED6_DT06/CH20089P._CP',             # 15
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclEvent(
        X                   = 1980,
        Y                   = -1000,
        Z                   = -1550,
        Range               = -2230,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFF056,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )


    ScpFunction(
        "Function_0_27A",          # 00, 0
        "Function_1_471",          # 01, 1
        "Function_2_4A6",          # 02, 2
        "Function_3_4BC",          # 03, 3
        "Function_4_503",          # 04, 4
        "Function_5_59D",          # 05, 5
        "Function_6_75A",          # 06, 6
        "Function_7_CAF",          # 07, 7
        "Function_8_4499",         # 08, 8
        "Function_9_5ED4",         # 09, 9
        "Function_10_5FDC",        # 0A, 10
        "Function_11_5FE7",        # 0B, 11
    )


    def Function_0_27A(): pass

    label("Function_0_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_288")
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_288")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_294"),
        (SWITCH_DEFAULT, "loc_2B5"),
    )


    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_2B2")

    Jump("loc_2B5")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_2DA")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    Jump("loc_2E9")

    label("loc_2DA")

    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)

    label("loc_2E9")

    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_302")
    Jump("loc_34E")

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_329")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -53080, 0, 12340, 3)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jump("loc_34E")

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_333")
    Jump("loc_34E")

    label("loc_333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_33D")
    Jump("loc_34E")

    label("loc_33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_347")
    Jump("loc_34E")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_34E")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_358")
    Jump("loc_470")

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_419")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, -52830, 0, 7650, 179)
    SetChrPos(0xA, -53810, 0, 7520, 79)
    SetChrPos(0xB, -5180, 0, 11510, 90)
    SetChrPos(0xD, -3130, 0, 13730, 262)
    SetChrPos(0xE, -5030, 0, 13030, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_END)), "loc_416")
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    SetChrChipByIndex(0xB, 20)
    SetChrChipByIndex(0xD, 20)
    SetChrChipByIndex(0xE, 20)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 21)

    label("loc_416")

    Jump("loc_470")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_423")
    Jump("loc_470")

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_42D")
    Jump("loc_470")

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_437")
    Jump("loc_470")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_441")
    Jump("loc_470")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_470")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_455")
    Jump("loc_470")

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_45F")
    Jump("loc_470")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_469")
    Jump("loc_470")

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_470")

    label("loc_470")

    Return()

    # Function_0_27A end

    def Function_1_471(): pass

    label("Function_1_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_486")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    OP_1B(0x2, 0x0, 0x7)

    label("loc_497")

    OP_1B(0x5, 0x0, 0xA)
    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_471 end

    def Function_2_4A6(): pass

    label("Function_2_4A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4A6")

    label("loc_4BB")

    Return()

    # Function_2_4A6 end

    def Function_3_4BC(): pass

    label("Function_3_4BC")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Duke Dunan is unconscious.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_4BC end

    def Function_4_503(): pass

    label("Function_4_503")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xA,
        (
            "#720FYour Majesty...and everyone else,\x01",
            "as well... Thank you for showing\x01",
            "mercy.\x02\x03",

            "His Grace will surely remember\x01",
            "this kindness once he awakens.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_503 end

    def Function_5_59D(): pass

    label("Function_5_59D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_5AA")
    Jump("loc_756")

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_731")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_637")

    ChrTalk(    #2
        0xFE,
        (
            "The princess is currently roaming\x01",
            "the city incognito.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "She says that some...'school friends'\x01",
            "of hers are visiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72E")

    label("loc_637")

    OP_A2(0x0)

    ChrTalk(    #4
        0xFE,
        (
            "The princess has returned, so I am presently\x01",
            "cleaning her room...for a dirty room, you see,\x01",
            "is not very welcoming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "The princess is currently roaming\x01",
            "the city incognito.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "She says that some...'school friends'\x01",
            "of hers are visiting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E")

    Jump("loc_756")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_73B")
    Jump("loc_756")

    label("loc_73B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_745")
    Jump("loc_756")

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_74F")
    Jump("loc_756")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_756")

    label("loc_756")

    TalkEnd(0xFE)
    Return()

    # Function_5_59D end

    def Function_6_75A(): pass

    label("Function_6_75A")

    EventBegin(0x0)
    OP_6D(-460, 0, 2620, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x138, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 10, 0, -5370, 225)
    SetChrPos(0x102, 10, 0, -5370, 225)
    SetChrPos(0x138, 10, 0, -5370, 225)

    def lambda_7D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_7D6)

    def lambda_7E8():
        OP_8E(0xFE, 0xFFFFFFA6, 0x0, 0x564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_7E8)
    Sleep(500)

    def lambda_808():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_808)

    def lambda_81A():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0xFFFFFE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81A)
    Sleep(500)

    def lambda_83A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_83A)

    def lambda_84C():
        OP_8E(0xFE, 0x2EE, 0x0, 0xFFFFFE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_84C)
    WaitChrThread(0x138, 0x1)
    OP_8C(0x138, 180, 400)

    ChrTalk(    #7
        0x101,
        (
            "#000FWhew...\x01",
            "That was intense.\x02\x03",

            "Thanks, Hilda.\x01",
            "You're a real lifesaver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#010FYeah, that was really well done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x138,
        (
            "#710FHa ha...\x01",
            "I'm just glad I could help.\x02\x03",

            "Now, then... Are you planning\x01",
            "to change your clothes before\x01",
            "going to see Her Majesty?\x02\x03",

            "If you'd prefer, I can just\x01",
            "show you the way now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#000FI think I'm okay as-is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        "#010FBoy clothes. Now.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-52690, 0, 7170, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x101, -51850, 0, 7470, 270)
    SetChrPos(0x102, -53280, 0, 7850, 180)
    SetChrPos(0x138, -52990, 0, 5970, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #12
        0x101,
        (
            "#000FOh, for the love of... Why are\x01",
            "you always so self-conscious?\x02\x03",

            "What was wrong with what\x01",
            "you had on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#010FIt's not an issue of self-consciousness.\x02\x03",

            "By the way, Hilda. Is this\x01",
            "room what I think it is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x138,
        (
            "#710FYes...\x01",
            "It is Princess Klaudia's bedroom.\x02\x03",

            "But she rarely sleeps in the\x01",
            "castle, so the room is all but\x01",
            "unused.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #15
        0x101,
        (
            "#000FHuh... No kidding?\x02\x03",

            "But I heard that the princess\x01",
            "was tending to the queen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x138,
        "#710F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#010FI guess that's just gossip, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x138,
        (
            "#710FYou'd have to ask Her Majesty\x01",
            "for the full details.\x02\x03",

            "Her room is on the second floor.\x02\x03",

            "I'll take you there.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)
    Return()

    # Function_6_75A end

    def Function_7_CAF(): pass

    label("Function_7_CAF")

    EventBegin(0x0)
    Fade(1000)
    OP_A2(0x644)
    OP_28(0x4A, 0x1, 0x100)
    OP_28(0x4A, 0x1, 0x200)
    SetChrChipByIndex(0x138, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x138, -950, 8000, 35250, 0)
    SetChrPos(0x101, -2110, 8000, 34000, 0)
    SetChrPos(0x102, -270, 8000, 34020, 0)
    SetChrPos(0x8, -980, 8000, 38840, 0)
    OP_6D(-570, 8000, 34880, 2000)

    ChrTalk(    #19
        0x138,
        (
            "#710FI beg your pardon, Your Majesty.\x02\x03",

            "I've brought the two I spoke of\x01",
            "before. This is Joshua and Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "Thank you kindly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "By all means, enter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x138,
        "#710FAs you wish.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x138, 0xFFFFF786, 0x1F40, 0x89B2, 0x7D0, 0x0)
    OP_8C(0x138, 180, 400)

    ChrTalk(    #23
        0x138,
        (
            "#710FI'll wait for you here.\x02\x03",

            "You two go on in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#000FR-Right...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        "#010FPardon us...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-100970, 0, 4310, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -100980, 0, 20410, 0)
    SetChrPos(0x101, -101650, 0, 3570, 0)
    SetChrPos(0x102, -100450, 0, 3560, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #26
        0x101,
        "#000FOh...\x02",
    )

    CloseMessageWindow()

    def lambda_ED2():
        OP_6D(-100940, 0, 19690, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ED2)

    def lambda_EEA():
        OP_6C(12000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EEA)

    def lambda_EFA():
        OP_67(0, 4200, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EFA)

    def lambda_F12():
        OP_6E(317, 8000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_F12)
    Sleep(6000)

    def lambda_F27():
        OP_8E(0xFE, 0xFFFE733E, 0x0, 0x39BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F27)

    def lambda_F42():
        OP_8E(0xFE, 0xFFFE797E, 0x0, 0x3AC0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F42)
    Sleep(2000)

    ChrTalk(    #27
        0x8,
        "#090F...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_8C(0x8, 180, 300)
    Sleep(1000)

    ChrTalk(    #28
        0x8,
        (
            "#090FHeehee...\x01",
            "I bid you welcome.\x02\x03",

            "My name is Alicia von Auslese.\x02\x03",

            "I am the twenty-sixth monarch\x01",
            "of the nation of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#000FU-Umm... I'm Estelle Bright.\x02\x03",

            "I'm a junior bracer of the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#010FAnd I'm Joshua Bright, of\x01",
            "the same affiliation.\x02\x03",

            "It is a great honor to meet you,\x01",
            "Your Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#090FEstelle and Joshua...\x02\x03",

            "I have truly been looking\x01",
            "forward to meeting you both.\x02\x03",

            "I regret that I cannot offer you\x01",
            "proper hospitality, but I have\x01",
            "prepared some tea.\x02\x03",

            "Please, have some and relax.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-106830, 640, 12020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(240, 0)
    SetChrPos(0x8, -106730, 0, 13420, 180)
    SetChrPos(0x101, -107390, 0, 10600, 0)
    SetChrPos(0x102, -106200, 0, 10610, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #32
        0x8,
        (
            "#090FI see... So Professor Russell asked\x01",
            "you to bring this information...\x02\x03",

            "A pitch-black orbment capable of\x01",
            "negating all other orbal energies...\x02\x03",

            "And you say that the colonel\x01",
            "has acquired it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#010FThe professor told us that you might\x01",
            "have some idea of what he intends to\x01",
            "do with it, Your Majesty.\x02\x03",

            "Can you tell us anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#090F...\x02\x03",

            "I have but a vague idea...\x02\x03",

            "But I did not think that the\x01",
            "colonel even knew of it.\x02\x03",

            "Perhaps I am worrying about\x01",
            "nothing...but even so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#000FExcuse me...but what is\x01",
            "this vague idea you have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#090F...I suppose there is no\x01",
            "harm in telling you.\x02\x03",

            "Some years ago, a massive orbal\x01",
            "reaction was detected beneath Grancel.\x02\x03",

            "Professor Russell was the individual\x01",
            "who came to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#000FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#010FDid this happen in the vicinity\x01",
            "of the sewers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#090FNo, far deeper underground\x01",
            "than that, in fact.\x02\x03",

            "Professor Russell was under the impression\x01",
            "that it might be a relic of the ancients\x01",
            "that still functioned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#000FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#010FSo...it was a bona fide artifact,\x01",
            "then?\x02\x03",

            "Most artifacts I know of have lost\x01",
            "their function, like the mechanisms\x01",
            "on top of the towers.\x02\x03",

            "But every now and again, you find\x01",
            "one that still functions--like\x01",
            "Mayor Dalmore's family heirloom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#000FAnd something like that\x01",
            "is beneath Grancel...\x02\x03",

            "So, what does that tell\x01",
            "us about the Black Orbment...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#010FMaybe...it could be used to halt\x01",
            "the artifact's functions?\x02\x03",

            "Could it do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#090FYes...\x02\x03",

            "However, we were unable to establish the nature\x01",
            "of the artifact, or indeed why it was buried\x01",
            "beneath the city.\x02\x03",

            "But it is beyond my imaginings how the colonel\x01",
            "could know of its existence...\x02\x03",

            "Professor Russell's research on it was kept\x01",
            "strictly confidential and off-the-record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#010FI see...\x02\x03",

            "In any event, it seems likely\x01",
            "that trouble is on the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#000FHonestly, just as I start to think maybe the\x01",
            "colonel might be a slightly nicer guy than we\x01",
            "were giving him credit for...\x02\x03",

            "But when someone's trying to stir up some\x01",
            "trouble, that's when us bracers come in!\x02\x03",

            "We won't let him get away with whatever evil\x01",
            "scheme he's trying to pull off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#090FHa ha...\x02\x03",

            "I'd expect no less from\x01",
            "Cassius' daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#000F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#010FYou're acquainted with our\x01",
            "father, Your Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#090FHe was a friend of my late son's, and a great\x01",
            "savior to the nation.\x02\x03",

            "Even after he retired from the army, he would\x01",
            "sometimes undertake requests for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#000FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        "#010FI didn't know that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#090FHa ha... I imagine that there\x01",
            "are a great many things about\x01",
            "him that you do not know.\x02\x03",

            "Including the precise role\x01",
            "he played in the war, ten\x01",
            "years ago...\x02\x03",

            "I assume you have not been told?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#000FWell...\x01",
            "Nothing super-detailed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#090FPerhaps, then, that is the role\x01",
            "that I am meant to play...\x02\x03",

            "Estelle and Joshua...\x02\x03",

            "Will you indulge me by\x01",
            "listening to an old story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#000FOh... Yes, absolutely!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        "#010FIt is no indulgence, Your Majesty.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()

    ChrTalk(    #58
        0x8,
        (
            "#090FTen years ago...\x02\x03",

            "A small farming village was\x01",
            "annihilated in the southern\x01",
            "reaches of the Erebonian Empire.\x02\x03",

            "It was neither natural disaster\x01",
            "nor monster attack, but some\x01",
            "unnatural atrocity.\x02\x03",

            "Since it happened so close to the national\x01",
            "border, the Empire decided that Liberl was\x01",
            "to blame, and declared open war.\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x4001B, 0x0, 0x0, 0x64)
    Sleep(300)

    ChrTalk(    #59
        0x8,
        (
            "#090FJust as the Empire made its declaration\x01",
            "of war, a massive military force breached\x01",
            "the Haken Gate.\x02\x03",

            "In what seemed like scant moments,\x01",
            "all of Liberl became occupied\x01",
            "territory, save for Grancel.\x02\x03",

            "It is said that the invasion\x01",
            "force was three times the size\x01",
            "of the entire Royal Army.\x02\x03",

            "Lingering doubts regarding the\x01",
            "massacre of the village kept the\x01",
            "other nations from intervening...\x02\x03",

            "Thus, it was but a matter of\x01",
            "time before Grancel, too,\x01",
            "would fall.\x02",
        )
    )

    CloseMessageWindow()
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001C, 0x0, 0x0, 0x64)

    ChrTalk(    #60
        0x8,
        (
            "#090FBut two months after the\x01",
            "outbreak of hostilities...\x02\x03",

            "...the war changed in a way that\x01",
            "none could have imagined.\x02\x03",

            "Patrol airships had just been developed and were\x01",
            "used to recapture Liberl's checkpoints, severing\x01",
            "the Imperial army's communications.\x02\x03",

            "The Royal Army then set about recapturing the\x01",
            "major regions one by one using ships launched\x01",
            "from Leiston Fortress.\x02\x03",

            "Zeiss, Ruan, Bose, Rolent...\x02\x03",

            "With their supply lines severed, the Erebonian\x01",
            "forces occupying each region were swiftly\x01",
            "crushed.\x02",
        )
    )

    CloseMessageWindow()
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001D, 0x0, 0x0, 0x64)

    ChrTalk(    #61
        0x8,
        (
            "#090FAnd the one behind this plan for\x01",
            "a counteroffensive was none other\x01",
            "than one Colonel Cassius Bright.\x02\x03",

            "It was your father, who was General Morgan's\x01",
            "right hand man at the time, as well Colonel\x01",
            "Richard's superior officer.\x02\x03",

            "Afterward, with the intercession of the Bracer\x01",
            "Guild and the Septian Church, the war was\x01",
            "brought to an end.\x02\x03",

            "But it was at this time that\x01",
            "Cassius lost what he treasured\x01",
            "most in all the world.\x02",
        )
    )

    CloseMessageWindow()
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001E, 0x0, 0x0, 0x64)

    ChrTalk(    #62
        0x8,
        (
            "#090FLena...your mother, Estelle.\x02\x03",

            "That clock tower was destroyed in\x01",
            "the Imperial Army's vain attempts\x01",
            "to hold back the counteroffensive.\x02\x03",

            "What followed, I am sure you know.\x02\x03",

            "Cassius was not even able to be by his wife's\x01",
            "side in her final moments...\x02",
        )
    )

    CloseMessageWindow()
    OP_AE(0x1F4)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #63
        0x101,
        (
            "#000FNo...\x02\x03",

            "I had no idea...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "#090FAnd he believed that the military operation\x01",
            "that he himself had planned effectively caused\x01",
            "her death.\x02\x03",

            "Blaming himself, he left the military and took\x01",
            "up the path of the bracer.\x02\x03",

            "All to stay with the only one he had left:\x01",
            "you.\x02\x03",

            "And this time, he swore he would be able to\x01",
            "protect those he loved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#000FDad...\x01",
            "That idiot...\x02\x03",

            "It wasn't his fault that Mom died...\x02\x03",

            "How could he even think that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        "#010FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#090FYes, you are correct...\x02\x03",

            "Given that all he lost was in\x01",
            "service to his country, the\x01",
            "responsibility falls upon me.\x02\x03",

            "And so, I am sorry, Estelle... I\x01",
            "failed to protect your mother...\x02\x03",

            "I have wished to apologize\x01",
            "to you for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#000FB-But you don't need to apologize!\x02\x03",

            "You've protected the peace of this country ever\x01",
            "since the war ended.\x02\x03",

            "The peace that Dad and all the other soldiers\x01",
            "who defended Liberl in the war fought so hard\x01",
            "to protect...\x02\x03",

            "And the peace that Mom gave her life for so\x01",
            "I could live in it.\x02\x03",

            "You have nothing to be sorry for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#090FEstelle... You have a kind\x01",
            "heart, and I am grateful.\x02\x03",

            "It gladdens my heart to have\x01",
            "finally met you in person...\x02\x03",

            "Now, more than ever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#000FYour Majesty...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "#090FHowever, that is why...\x02\x03",

            "That is why I do not wish you\x01",
            "to put yourself in danger.\x02\x03",

            "If some tragedy were to befall you\x01",
            "in Cassius' absence, I know of no\x01",
            "apology that could ever suffice.\x02\x03",

            "That is why I would like for you\x01",
            "to remove yourself from any\x01",
            "dealings with this matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#000FB-But...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        (
            "#010FIf I may, Your Majesty...\x02\x03",

            "The peace that Dad restored and that\x01",
            "you protect, though it has held firm,\x01",
            "now trembles like a leaf in the breeze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        "#090FJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#010FIf the colonel is able to use the Black Orbment for\x01",
            "whatever purpose he intends...\x02\x03",

            "...and if he succeeds in making the duke the new\x01",
            "king of Liberl, then what will become of that\x01",
            "peace?\x02\x03",

            "I ask only that you consider that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "#090F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#000FY-Your Majesty...?\x02\x03",

            "Right when we became junior\x01",
            "bracers, we inherited a whole\x01",
            "lot of work from Dad.\x02\x03",

            "After the sky bandit incident, we got that\x01",
            "letter and the package, and we've been\x01",
            "running all around creation ever since...\x02\x03",

            "It feels to us like our Dad's\x01",
            "been nudging us in the back\x01",
            "this whole time.\x02\x03",

            "That's why I want to defend peace...\x02\x03",

            "So that everyone we've met, and\x01",
            "everyone we care about...\x02\x03",

            "...can go on living secure\x01",
            "and happy lives.\x02\x03",

            "Just like you...and just like Mom and Dad...\x01",
            "I'm doing this because it's what I believe is\x01",
            "right. And I really want to see it through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#090FEstelle...\x02\x03",

            "...\x02\x03",

            "It seems...she was right\x01",
            "about you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "#090FI, too, am ready.\x02\x03",

            "I would like for the two of\x01",
            "you to carry my request to\x01",
            "the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#000FYour Majesty...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        (
            "#010FMy Liege...\x01",
            "We will do whatever you ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "#090FMy request is for the Bracer Guild to rescue\x01",
            "those being held captive by the Intelligence\x01",
            "Division.\x02\x03",

            "Amongst them is my granddaughter, Klaudia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#000FAh-ha. So the princess IS being\x01",
            "held captive somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "#090FYes...\x02\x03",

            "This coup d'etat started when\x01",
            "I backed her as the successor\x01",
            "to the throne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        (
            "#010FIn other words, Duke Dunan\x01",
            "was out of the running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#090FYes... Though he is my nephew,\x01",
            "he is possessed of a considerable\x01",
            "number of character flaws.\x02\x03",

            "In brief, where he is lacking,\x01",
            "my granddaughter shines.\x02\x03",

            "For the sake of this nation's\x01",
            "future, I would have my\x01",
            "granddaughter succeed me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#000FWell...um, I don't actually\x01",
            "know her...\x02\x03",

            "But I personally lean toward the\x01",
            "idea that your judgment should\x01",
            "REALLY be trusted here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#090FHa ha... However, there are those\x01",
            "who object strongly to a woman\x01",
            "wielding political power.\x02\x03",

            "Not to mention, the memory of\x01",
            "the invasion by a larger power\x01",
            "is still relatively fresh...\x02\x03",

            "Some of them will perceive a\x01",
            "succession of two consecutive\x01",
            "queens to be a sign of weakness.\x02\x03",

            "It is hardly surprising that\x01",
            "such a notion has taken root\x01",
            "in the minds of some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        (
            "#010F'Some' including Colonel Richard,\x01",
            "I presume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#090FQuite right.\x02\x03",

            "Klaudia's pending succession\x01",
            "to the throne caught him\x01",
            "quite unawares.\x02\x03",

            "That, along with his passing of\x01",
            "this information to the duke,\x01",
            "is what led to this coup.\x02\x03",

            "This was all staged so that Liberl would\x01",
            "become a strong military power, with\x01",
            "the colonel ruling from the shadows...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x102,
        (
            "#010FI see...\x02\x03",

            "That finally lets us see\x01",
            "the whole picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#000FSo if Liberl became a militarized\x01",
            "country...what would happen then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        (
            "#010FA great many things.\x02\x03",

            "Taxes would be levied to\x01",
            "fill the war chest...\x02\x03",

            "Orbal weaponry would be developed\x01",
            "with the express intent of causing\x01",
            "havoc on a massive scale...\x02\x03",

            "A wide-ranging policy of conscription\x01",
            "would be adopted...\x02\x03",

            "And no doubt contracting jaeger corps would\x01",
            "be made legal, which is not the case at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#000FOh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#090FIndeed, the colonel has made\x01",
            "very adamant requests that I\x01",
            "enact such policies.\x02\x03",

            "I thought that such proposals\x01",
            "were born out of genuine love\x01",
            "for his country...\x02\x03",

            "...but I never agreed that\x01",
            "they were the right course\x01",
            "of action to take.\x02\x03",

            "The Royal Army is not all\x01",
            "that protects this land.\x02\x03",

            "We have worked hard to maintain\x01",
            "treaties with other countries.\x02\x03",

            "Defending a nation goes hand in hand with\x01",
            "free cultural exchange and trade with all\x01",
            "other nations, to the benefit of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#010FI feel the same way, Your Majesty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#000FYeah! Makes sense to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "#090FThe colonel, however, finds\x01",
            "such notions to be womanly\x01",
            "and foolishly idealistic.\x02\x03",

            "And so he demanded that I abdicate the throne\x01",
            "in exchange for Klaudia's safe return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#000F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#090FMany people have had family members\x01",
            "taken to ensure that they would\x01",
            "not dare to oppose the colonel.\x02\x03",

            "But I am the queen. And I will not allow\x01",
            "all that I love about my country to be\x01",
            "destroyed, simply because of blood ties.\x02\x03",

            "Still...she is my only granddaughter...\x02\x03",

            "I cannot simply allow her to die...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#000FYour Majesty...please try to relax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        (
            "#010FWe hear and comply with\x01",
            "your request.\x02\x03",

            "We will see to it that the princess\x01",
            "is rescued from those who have\x01",
            "imprisoned her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#090FThank you...both of you.\x02\x03",

            "With that reassurance, I will do all I can\x01",
            "to oppose the colonel's demands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#000FU-Umm... H-Have you any other\x01",
            "requests, Your Majesty?\x02\x03",

            "The Black Orbment still has\x01",
            "to be dealt with...\x02\x03",

            "And I don't think we should\x01",
            "just leave you here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#090FI appreciate your sentiment, Estelle.\x02\x03",

            "But the present state of affairs\x01",
            "is not contingent upon my freedom\x01",
            "or imprisonment.\x02\x03",

            "The Gospel shall continue to weigh\x01",
            "heavily on my mind, for a great\x01",
            "many reasons...\x02\x03",

            "For my part, I will attempt to\x01",
            "ascertain the colonel's true\x01",
            "intentions with it.\x02\x03",

            "I ask that you try to comply\x01",
            "with my feelings on the matter.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-52350, 0, 6280, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x138, 0)
    SetChrPos(0x101, -53470, 0, 6160, 90)
    SetChrPos(0x102, -51450, 0, 6000, 270)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #107
        0x101,
        (
            "#000F*sigh*... Wow, what a totally\x01",
            "awesome person.\x02\x03",

            "Super-nice, but with a\x01",
            "seriously strong will.\x02\x03",

            "I hope I'm even one-tenth\x01",
            "that cool when I get old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        (
            "#010F'Cool.' Did you actually just\x01",
            "call the queen that?\x02\x03",

            "Still, she definitely has what it\x01",
            "takes to govern a whole country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#000FYeah...\x02\x03",

            "I really want to stop this\x01",
            "coup thingy and help her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        (
            "#010FThat's definitely outside\x01",
            "of bracer jurisdiction.\x02\x03",

            "Well, first things first.\x01",
            "We do whatever we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#000FRight.\x02\x03",

            "But you know, I'm still freaking\x01",
            "out about what the queen told\x01",
            "us about Dad.\x02\x03",

            "I wonder if she's got any more\x01",
            "tidbits she'd be willing to share...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        "#010FPerhaps so.\x02",
    )

    CloseMessageWindow()
    OP_9F(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x138, -51030, 0, 420, 225)

    ChrTalk(    #113
        0x138,
        (
            "#710FEstelle and Joshua...\x02\x03",

            "Have you finished changing?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42CF():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42CF)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #114
        0x101,
        "#000FOh, yeah.\x02",
    )

    CloseMessageWindow()

    def lambda_42F8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_42F8)

    def lambda_430A():
        OP_8E(0xFE, 0xFFFF34A4, 0x0, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_430A)

    def lambda_4325():

        label("loc_4325")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_4325")

    QueueWorkItem2(0x101, 1, lambda_4325)

    def lambda_4336():

        label("loc_4336")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_4336")

    QueueWorkItem2(0x102, 1, lambda_4336)
    Sleep(300)
    OP_6D(-52330, 0, 5310, 1000)
    WaitChrThread(0x138, 0x1)

    ChrTalk(    #115
        0x138,
        (
            "#710FThen we should return to\x01",
            "the waiting room at once.\x02\x03",

            "It's already after eleven o'clock.\x01",
            "Actually, it's almost midnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#000FWhoa...\x01",
            "Is it really that late?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#010FThe queen spoke with\x01",
            "us for a long time.\x02\x03",

            "If we stay any longer, it's apt\x01",
            "to make the guards suspicious.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    OP_1B(0x2, 0x0, 0xFFFF)
    Return()

    # Function_7_CAF end

    def Function_8_4499(): pass

    label("Function_8_4499")

    ClearMapFlags(0x10000000)
    OP_28(0x4E, 0x1, 0x4)
    EventBegin(0x0)
    OP_6D(1080, 0, 3170, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(44000, 0)
    OP_6E(426, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 0, 0, 9760, 180)
    SetChrPos(0xB, -1480, 0, 9280, 180)
    SetChrPos(0xD, 0, 0, 8350, 180)
    SetChrPos(0xE, 1400, 0, 9310, 180)
    SetChrPos(0x101, -90, 0, 920, 0)
    SetChrPos(0x105, -1330, 0, 430, 0)
    SetChrPos(0x103, 930, 0, 430, 0)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x103, 11)
    SetChrChipByIndex(0x105, 13)
    FadeToBright(1000, 0)
    OP_6D(1130, 0, 6000, 1000)

    ChrTalk(    #118
        0x9,
        (
            "#224FTr-traitors!\x01",
            "You dare to come here?!\x02\x03",

            "Do you not realize that\x01",
            "I am the new king?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#509F#2POh, go brush your goofy hairdo.\x02\x03",

            "You ain't king YET.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        "#226FWh-WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x103,
        (
            "#020F#2PYour Grace, Duke Dunan.\x01",
            "We are with the Bracer Guild.\x02\x03",

            "At the request of Her Highness, \x01",
            "Princess Klaudia, we are here \x01",
            "to free the queen!\x02\x03",

            "#021FIt would be best for all involved\x01",
            "if you quietly stood aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x9,
        (
            "#222FK-Klaudia?!\x02\x03",

            "Damn that brat!\x01",
            "Damn her to hell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x105,
        (
            "#043F#2PUncle Dunan...please, stop this.\x02\x03",

            "Colonel Richard is just using you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "#223FWha... Who are you...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #125
        0x9,
        "#222FKuh... Kuh...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #126
        0x9,
        "#224F#3SKlaudia, is that you?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #127
        0x9,
        (
            "#226FWhat happened to your hair?!\x01",
            "And your clothes?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#007F#2PWe have comprehension! \x01",
            "Repeat, we have comprehension!\x02\x03",

            "Though he still hasn't noticed\x01",
            "that we first met him in Ruan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x103,
        (
            "#027F#2PNo idea what you're talking\x01",
            "about...but he doesn't seem\x01",
            "the most observant sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x105,
        (
            "#542F#2PI should have told him sooner,\x01",
            "perhaps...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x9,
        (
            "#226FH-How dare you make\x01",
            "a fool of me?!\x02\x03",

            "It's because of things like this that\x01",
            "those creatures known as 'women'\x01",
            "are not to be trusted!\x02\x03",

            "Sly, narrow-minded, nit-picking,\x01",
            "nagging wretches...\x02\x03",

            "How could I ever give up the\x01",
            "crown to such a vile creature?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#002F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x103,
        "#024F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x105,
        "#043F#2P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #135
        0x9,
        "#223F...Err... I mean...\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #136
        0xB,
        (
            "#3PY-Your Grace... I don't think\x01",
            "that was the right thing to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xD,
        "#3PM-Maybe you should apologize...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_63(0x105)
    OP_63(0x103)

    ChrTalk(    #138
        0x101,
        (
            "#001F#2PHmmm...\x01",
            "'Vile creatures,' huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#021F#2PMy, my. I believe you've just\x01",
            "gone from stupid to suicidal.\x02\x03",

            "After all, that's a mighty courageous\x01",
            "sentiment to vocalize when in the\x01",
            "presence of three ARMED women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x105,
        (
            "#542F#2PI... I'm sorry, Uncle.\x02\x03",

            "#045FIn this, I cannot defend you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D01():
        OP_6D(420, 0, 10250, 700)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D01)

    def lambda_4D19():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D19)
    Sleep(50)

    def lambda_4D39():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D39)
    Sleep(50)

    def lambda_4D59():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D59)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    Battle(0x3AA, 0x0, 0x0, 0x2, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4D98"),
        (SWITCH_DEFAULT, "loc_4D9B"),
    )


    label("loc_4D98")

    OP_B4(0x0)
    Return()

    label("loc_4D9B")

    EventBegin(0x0)
    OP_6D(-2360, 0, 10280, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0xB, -5180, 0, 11510, 90)
    SetChrPos(0xD, -3130, 0, 13730, 262)
    SetChrPos(0xE, -5030, 0, 13030, 135)
    SetChrChipByIndex(0xB, 20)
    SetChrChipByIndex(0xD, 20)
    SetChrChipByIndex(0xE, 20)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E5A")
    SetChrPos(0x9, -4810, 0, 7920, 90)
    Jump("loc_4E80")

    label("loc_4E5A")

    SetChrPos(0x9, -6370, 0, 7980, 90)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 21)

    label("loc_4E80")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4E8C"),
        (SWITCH_DEFAULT, "loc_57E4"),
    )


    label("loc_4E8C")

    SetChrPos(0x101, -2120, 0, 8860, 0)
    SetChrPos(0x105, -850, 0, 8130, 0)
    SetChrPos(0x103, -2400, 0, 7180, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_2B(0x4D, 0x2)

    ChrTalk(    #141
        0x101,
        (
            "#502F#4PWell, that settles that!\x02\x03",

            "#006FNow, then, shall I show you just\x01",
            "how 'vile' a woman can be?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F3C():
        OP_6D(-5080, 0, 8690, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F3C)

    def lambda_4F54():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F54)
    Sleep(50)

    def lambda_4F67():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F67)
    Sleep(50)

    def lambda_4F7A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F7A)
    OP_8F(0x9, 0xFFFFEA34, 0x0, 0x1F18, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #142
        0x103,
        (
            "#027F#4PMaybe I should give him a taste\x01",
            "of a ladylike whipping.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x9, 0xFFFFE6E2, 0x0, 0x1EB4, 0x7D0, 0x0)

    ChrTalk(    #143
        0x9,
        (
            "#226FEe...eeeeeeeeep...\x02\x03",

            "S-Stay back!\x01",
            "Please, stay awaaay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x105,
        (
            "#045FUm... I might be able\x01",
            "to call them off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x9,
        (
            "#222FI-If you do, I swear I'll be Her Majesty's\x01",
            "very own human shield!\x02\x03",

            "#224FAAAIEEEE! MOMMY!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_50E3():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_50E3)
    OP_8F(0x9, 0xFFFFDFC6, 0x0, 0x1EDC, 0x1770, 0x0)
    OP_22(0x7D, 0x0, 0x64)

    ChrTalk(    #146 op#A op#5
        0x9,
        "#6P#228F#10AHurrrrk...buurrrgggle...\x05\x02",
    )


    def lambda_5134():
        OP_8C(0xFE, 800, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5134)
    OP_96(0x9, 0xFFFFE462, 0x0, 0x1F2C, 0x320, 0x1F40)

    def lambda_5159():
        OP_8C(0xFE, 800, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5159)
    OP_96(0x9, 0xFFFFE71E, 0x0, 0x1F2C, 0x190, 0x1F40)
    OP_22(0x30, 0x0, 0x64)
    OP_62(0x9, 0x12C, 1600, 0x30, 0x32, 0x96, 0x0)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 21)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)

    def lambda_520D():
        OP_6D(-5790, 0, 8440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_520D)

    def lambda_5225():
        OP_8E(0xFE, 0xFFFFE94E, 0x0, 0x245E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5225)
    Sleep(200)

    def lambda_5245():
        OP_8E(0xFE, 0xFFFFECD2, 0x0, 0x1C84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5245)
    Sleep(200)

    def lambda_5265():
        OP_8E(0xFE, 0xFFFFEE30, 0x0, 0x22A6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5265)

    def lambda_5280():

        label("loc_5280")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_5280")

    QueueWorkItem2(0x101, 1, lambda_5280)

    def lambda_5291():

        label("loc_5291")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_5291")

    QueueWorkItem2(0x103, 1, lambda_5291)

    def lambda_52A2():

        label("loc_52A2")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_52A2")

    QueueWorkItem2(0x105, 1, lambda_52A2)
    WaitChrThread(0x101, 0x2)
    OP_63(0x9)

    ChrTalk(    #147
        0x101,
        (
            "#007FOops... Maybe we overdid\x01",
            "it with the threats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x103,
        (
            "#021FWell, a little dose of the cold,\x01",
            "hard truth might be the best\x01",
            "medicine he ever gets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x105,
        (
            "#047FYes... It is an unfortunate situation\x01",
            "he's gotten himself into.\x02\x03",

            "#049FStill, I cannot allow my unconscious\x01",
            "uncle to simply be lef--\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -490, 0, -530, 270)
    OP_4A(0xA, 255)

    NpcTalk(    #150
        0xA,
        "Man's Voice",
        "#1P...Y-Your Grace?!\x02",
    )

    CloseMessageWindow()

    def lambda_5420():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5420)

    def lambda_542E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_542E)

    def lambda_543C():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_543C)

    def lambda_544A():
        OP_8E(0xA, 0xFFFFE73C, 0x0, 0x1C7A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_544A)
    OP_6D(-2009, 0, 6520, 1000)
    Sleep(200)

    def lambda_547B():

        label("loc_547B")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_547B")

    QueueWorkItem2(0x101, 1, lambda_547B)

    def lambda_548C():

        label("loc_548C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_548C")

    QueueWorkItem2(0x103, 1, lambda_548C)

    def lambda_549D():

        label("loc_549D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_549D")

    QueueWorkItem2(0x105, 1, lambda_549D)

    def lambda_54AE():
        OP_6D(-5850, 0, 8290, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_54AE)
    WaitChrThread(0xA, 0x1)
    TurnDirection(0xA, 0x9, 800)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #151
        0x101,
        "#004FHi, Phillip!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x105, 400)

    ChrTalk(    #152
        0xA,
        (
            "#722FMiss Estelle...and Your Highness?!\x02\x03",

            "I can offer no words to make\x01",
            "up for my master's behavior\x01",
            "in this instance!\x02\x03",

            "As the man who raised him,\x01",
            "the responsibility is mine\x01",
            "to bear!\x02\x03",

            "#723FPlease, I ask that you \x01",
            "punish me in his stead!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #153
        "\x07\x05Phillip bowed his head deeply.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #154
        0x101,
        "#004FH-Hey! Hold on a second!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x105,
        (
            "#048FPlease, Phillip...\x01",
            "Lift your eyes.\x02\x03",

            "We're here to help my grandmother...\x01",
            "to save the queen.\x02\x03",

            "We have no intention of\x01",
            "doing anything to the duke.\x02\x03",

            "I would appreciate it if you\x01",
            "would take him to my room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xA,
        "#721FY-Your Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x103,
        (
            "#020FHe's not actually hurt.\x02\x03",

            "He just passed out from the shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xA,
        (
            "#722FTh-Thank you so much...\x01",
            "All of you...\x02\x03",

            "I will not forget the boon\x01",
            "you've granted!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E19")

    label("loc_57E4")

    SetChrPos(0x101, -5810, 0, 9310, 315)
    SetChrPos(0x105, -4910, 0, 7300, 336)
    SetChrPos(0x103, -4560, 0, 8870, 296)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    OP_6D(-5790, 0, 8440, 0)

    def lambda_583D():

        label("loc_583D")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_583D")

    QueueWorkItem2(0x101, 1, lambda_583D)

    def lambda_584E():

        label("loc_584E")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_584E")

    QueueWorkItem2(0x103, 1, lambda_584E)

    def lambda_585F():

        label("loc_585F")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_585F")

    QueueWorkItem2(0x105, 1, lambda_585F)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #159
        0x101,
        (
            "#007FWhew... I thought he was going\x01",
            "to go belly-up on us, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x103,
        (
            "#020FI really only wanted to beat on\x01",
            "the Special Ops soldiers...\x02\x03",

            "#021FWell, a little dose of the cold,\x01",
            "hard truth might be the best\x01",
            "medicine he ever gets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x105,
        (
            "#047FYes... It is an unfortunate situation\x01",
            "he's gotten himself into.\x02\x03",

            "#049FStill, I cannot allow my unconscious\x01",
            "uncle to simply be lef--\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -490, 0, -530, 270)
    OP_4A(0xA, 255)

    NpcTalk(    #162
        0xA,
        "Man's Voice",
        "#1P...Y-Your Grace?!\x02",
    )

    CloseMessageWindow()

    def lambda_5A2D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A2D)

    def lambda_5A3B():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A3B)

    def lambda_5A49():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A49)

    def lambda_5A57():
        OP_8E(0xA, 0xFFFFE73C, 0x0, 0x1C7A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5A57)
    OP_6D(-2009, 0, 6520, 1000)
    Sleep(200)

    def lambda_5A88():

        label("loc_5A88")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5A88")

    QueueWorkItem2(0x101, 1, lambda_5A88)

    def lambda_5A99():

        label("loc_5A99")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5A99")

    QueueWorkItem2(0x103, 1, lambda_5A99)

    def lambda_5AAA():

        label("loc_5AAA")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5AAA")

    QueueWorkItem2(0x105, 1, lambda_5AAA)

    def lambda_5ABB():
        OP_6D(-5850, 0, 8290, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5ABB)
    WaitChrThread(0xA, 0x1)
    TurnDirection(0xA, 0x9, 800)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #163
        0x101,
        "#004FHi, Phillip!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x105, 400)

    ChrTalk(    #164
        0xA,
        (
            "#722FMiss Estelle...and Your Highness?!\x02\x03",

            "I can offer no words to make\x01",
            "up for my master's behavior\x01",
            "in this instance!\x02\x03",

            "As the man who raised him,\x01",
            "the responsibility is mine\x01",
            "to bear!\x02\x03",

            "#723FPlease, I ask that you \x01",
            "punish me in his stead!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #165
        "\x07\x05Phillip bowed his head deeply.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #166
        0x101,
        "#004FH-Hey! Hold on a second!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x105,
        (
            "#048FPlease, Phillip...\x01",
            "Lift your eyes.\x02\x03",

            "We're here to help my grandmother...\x01",
            "to save the queen.\x02\x03",

            "We have no intention of\x01",
            "doing anything to the duke.\x02\x03",

            "I would appreciate it if you\x01",
            "would take him to my room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        "#721FY-Your Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x103,
        (
            "#020FHe's not actually hurt.\x02\x03",

            "It was just shock at the thought\x01",
            "of someone actually laying a\x01",
            "hand on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "#722FTh-Thank you so much...\x01",
            "All of you...\x02\x03",

            "I will not forget the boon\x01",
            "you've granted!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E19")

    label("loc_5E19")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x9, -52830, 0, 7650, 179)
    SetChrPos(0xA, -53810, 0, 7520, 79)
    OP_63(0x9)
    OP_6D(-5920, 0, 8680, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    SetChrPos(0x101, -5920, 0, 8680, 0)
    SetChrPos(0x105, -5920, 0, 8680, 0)
    SetChrPos(0x103, -5920, 0, 8680, 0)
    FadeToBright(1000, 0)
    OP_A2(0x665)
    EventEnd(0x0)
    Return()

    # Function_8_4499 end

    def Function_9_5ED4(): pass

    label("Function_9_5ED4")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x103, 11)
    SetChrChipByIndex(0x105, 13)
    OP_6D(-100980, 0, 8360, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -101110, 0, 3990, 0)
    SetChrPos(0x103, -102060, 0, 2930, 0)
    SetChrPos(0x105, -100330, 0, 2930, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #171
        0x101,
        "#000F誰もいない？！（※仮）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x105,
        "#040Fきっと、奥のテラスです！（※仮）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x680)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    EventEnd(0x0)
    Return()

    # Function_9_5ED4 end

    def Function_10_5FDC(): pass

    label("Function_10_5FDC")

    ClearMapFlags(0x2000000)
    OP_1B(0x5, 0x0, 0xFFFF)
    Return()

    # Function_10_5FDC end

    def Function_11_5FE7(): pass

    label("Function_11_5FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_606E")
    EventBegin(0x1)
    TurnDirection(0x138, 0x101, 400)

    NpcTalk(    #173
        0x0,
        "Head Maid Hilda",
        (
            "#710FHer Majesty's room is on the second\x01",
            "floor of the Royal Keep.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_606E")

    Return()

    # Function_11_5FE7 end

    SaveToFile()

Try(main)
