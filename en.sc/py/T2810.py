from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2810   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2810.x',
        MapIndex            = 1,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Mr. Ratio',                            # 9
        'Ms. Wiola',                            # 10
        'Ms. Millia',                           # 11
        'Dean Collins',                         # 12
        'Argyle',                               # 13
        'Janitor Parkes',                       # 14
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
        'ED6_DT07/CH01663 ._CH',             # 00
        'ED6_DT07/CH01213 ._CH',             # 01
        'ED6_DT07/CH01433 ._CH',             # 02
        'ED6_DT07/CH02603 ._CH',             # 03
        'ED6_DT07/CH01360 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01663P._CP',             # 00
        'ED6_DT07/CH01213P._CP',             # 01
        'ED6_DT07/CH01433P._CP',             # 02
        'ED6_DT07/CH02603P._CP',             # 03
        'ED6_DT07/CH01360P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
    )

    DeclNpc(
        X                   = 87640,
        Z                   = 200,
        Y                   = 2820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 84430,
        Z                   = 200,
        Y                   = 1120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 84510,
        Z                   = 200,
        Y                   = 2890,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 200,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 2540,
        Z                   = 0,
        Y                   = 33300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2120,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    DeclActor(
        TriggerX            = 116010,
        TriggerZ            = 0,
        TriggerY            = 2750,
        TriggerRange        = 400,
        ActorX              = 116010,
        ActorZ              = 1700,
        ActorY              = 4800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1E3",          # 01, 1
        "Function_2_1E4",          # 02, 2
        "Function_3_2A6",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_744",          # 05, 5
        "Function_6_7BD",          # 06, 6
        "Function_7_836",          # 07, 7
        "Function_8_89C",          # 08, 8
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Return()

    # Function_0_1E2 end

    def Function_1_1E3(): pass

    label("Function_1_1E3")

    Return()

    # Function_1_1E3 end

    def Function_2_1E4(): pass

    label("Function_2_1E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22C")

    ChrTalk(    #0
        0xFE,
        (
            "Surprising to see someone\x01",
            "here at this time of night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2")

    label("loc_22C")

    OP_A2(0x2)

    ChrTalk(    #1
        0xFE,
        (
            "What are you all doing out\x01",
            "this late?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Me? Just making sure everything's\x01",
            "properly locked up before break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2")

    TalkEnd(0xFE)
    Return()

    # Function_2_1E4 end

    def Function_3_2A6(): pass

    label("Function_3_2A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_310")

    ChrTalk(    #3
        0xFE,
        (
            "If you don't need anything,\x01",
            "leave me be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Don't steal my precious solitude.\x01",
            "Please?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A9")

    label("loc_310")

    OP_A2(0x1)

    ChrTalk(    #5
        0xFE,
        (
            "Heh heh heh...\x01",
            "The darkness is so calming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Being in a lonely schoolhouse in\x01",
            "the dead of night is everything I'd\x01",
            "pictured it to be: perfect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A9")

    TalkEnd(0xFE)
    Return()

    # Function_3_2A6 end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43D")
    Jump("loc_47F")

    label("loc_43D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_459")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_47F")

    label("loc_459")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_475")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_47F")

    label("loc_475")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_47F")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_73B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_504")

    ChrTalk(    #7
        0xB,
        (
            "#780FThere may be monsters hiding\x01",
            "in the old schoolhouse.\x02\x03",

            "Do be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B")

    label("loc_504")

    OP_A2(0x0)

    ChrTalk(    #8
        0xB,
        (
            "#780FI've heard from the staff that\x01",
            "you're going to investigate the\x01",
            "old schoolhouse.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x105, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58E")
    SetChrSubChip(0xB, 1)
    Jump("loc_5B4")

    label("loc_58E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AF")
    SetChrSubChip(0xB, 2)
    Jump("loc_5B4")

    label("loc_5AF")

    SetChrSubChip(0xB, 0)

    label("loc_5B4")

    OP_8C(0xB, 180, 0)
    SetChrFlags(0xB, 0x10)
    Sleep(200)

    ChrTalk(    #9
        0xB,
        "#780FKloe, will you be going, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        (
            "#040FYes. I know it best out of all\x01",
            "of us, so I'd like to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        "#780FI see. Very well.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_664")
    TurnDirection(0xB, 0x103, 0)
    Jump("loc_66B")

    label("loc_664")

    TurnDirection(0xB, 0x106, 0)

    label("loc_66B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68C")
    SetChrSubChip(0xB, 1)
    Jump("loc_6B2")

    label("loc_68C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AD")
    SetChrSubChip(0xB, 2)
    Jump("loc_6B2")

    label("loc_6AD")

    SetChrSubChip(0xB, 0)

    label("loc_6B2")

    OP_8C(0xB, 180, 0)
    SetChrFlags(0xB, 0x10)
    Sleep(200)

    ChrTalk(    #12
        0xB,
        (
            "#780FEveryone, take care of Kloe,\x01",
            "won't you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_71A")

    ChrTalk(    #13
        0x103,
        "#020FLeave her to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_73B")

    label("loc_71A")


    ChrTalk(    #14
        0x106,
        "#050FYeah, leave her to us.\x02",
    )

    CloseMessageWindow()

    label("loc_73B")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_4_3AD end

    def Function_5_744(): pass

    label("Function_5_744")

    TalkBegin(0xFE)

    ChrTalk(    #15
        0xFE,
        (
            "My class really gave it their\x01",
            "all on the exams!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I think we may have even\x01",
            "beaten Wiola's class, heh heh.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_744 end

    def Function_6_7BD(): pass

    label("Function_6_7BD")

    TalkBegin(0xFE)

    ChrTalk(    #17
        0xFE,
        (
            "My class did a most wonderful\x01",
            "job this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I'm certain that we beat Millia's\x01",
            "class at the very least.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_7BD end

    def Function_7_836(): pass

    label("Function_7_836")

    TalkBegin(0xFE)

    ChrTalk(    #19
        0xFE,
        (
            "*pheeew* Finally done with\x01",
            "grading that fat stack of papers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "Man, my neck is sore...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_836 end

    def Function_8_89C(): pass

    label("Function_8_89C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #21
        "\x07\x05Quiet in the halls! -Student Council\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_89C end

    SaveToFile()

Try(main)
