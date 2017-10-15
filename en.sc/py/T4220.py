from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4220   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4220.x',
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
        'General Morgan',                       # 10
        'Scherazard',                           # 11
        'Olivier',                              # 12
        'Princess Klaudia',                     # 13
        'Agate',                                # 14
        'Tita',                                 # 15
        'Zin',                                  # 16
        'Father Kevin',                         # 17
        'Cassius',                              # 18
        'Captain Schwarz',                      # 19
        'Royal Army Officer',                   # 20
        'Sieg',                                 # 21
        'Lt. Colonel Cid',                      # 22
        'Richard',                              # 23
        'Royal Guardsman',                      # 24
        'Cassius',                              # 25
        'Primrose',                             # 26
        'Targeting Camera',                     # 27
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
        'ED6_DT07/CH02013 ._CH',             # 00
        'ED6_DT07/CH02080 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00050 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH00070 ._CH',             # 07
        'ED6_DT27/CH03080 ._CH',             # 08
        'ED6_DT27/CH03670 ._CH',             # 09
        'ED6_DT27/CH03580 ._CH',             # 0A
        'ED6_DT07/CH01600 ._CH',             # 0B
        'ED6_DT07/CH02010 ._CH',             # 0C
        'ED6_DT26/CH20411 ._CH',             # 0D
        'ED6_DT26/CH20432 ._CH',             # 0E
        'ED6_DT07/CH00041 ._CH',             # 0F
        'ED6_DT07/CH00061 ._CH',             # 10
        'ED6_DT07/CH01350 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH02013P._CP',             # 00
        'ED6_DT07/CH02080P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00050P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH00070P._CP',             # 07
        'ED6_DT27/CH03080P._CP',             # 08
        'ED6_DT27/CH03670P._CP',             # 09
        'ED6_DT27/CH03580P._CP',             # 0A
        'ED6_DT07/CH01600P._CP',             # 0B
        'ED6_DT07/CH02010P._CP',             # 0C
        'ED6_DT26/CH20411P._CP',             # 0D
        'ED6_DT26/CH20432P._CP',             # 0E
        'ED6_DT07/CH00041P._CP',             # 0F
        'ED6_DT07/CH00061P._CP',             # 10
        'ED6_DT07/CH01350P._CP',             # 11
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 320,
        Z                   = 0,
        Y                   = 141880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_39A",          # 00, 0
        "Function_1_3F1",          # 01, 1
        "Function_2_417",          # 02, 2
        "Function_3_43B",          # 03, 3
        "Function_4_62A",          # 04, 4
        "Function_5_4276",         # 05, 5
        "Function_6_42BC",         # 06, 6
        "Function_7_42E7",         # 07, 7
        "Function_8_4312",         # 08, 8
        "Function_9_4333",         # 09, 9
        "Function_10_4354",        # 0A, 10
        "Function_11_4375",        # 0B, 11
        "Function_12_4396",        # 0C, 12
        "Function_13_43B7",        # 0D, 13
        "Function_14_43E2",        # 0E, 14
        "Function_15_440D",        # 0F, 15
    )


    def Function_0_39A(): pass

    label("Function_0_39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_3A9")
    SetChrFlags(0x19, 0x80)
    Jump("loc_3B5")

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3B5")
    SetChrFlags(0x19, 0x80)

    label("loc_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3D4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_3F0")

    label("loc_3D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3F0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_3F0")

    Return()

    # Function_0_39A end

    def Function_1_3F1(): pass

    label("Function_1_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40D")
    OP_B1("t4220_y")
    Jump("loc_416")

    label("loc_40D")

    OP_B1("t4220_n")

    label("loc_416")

    Return()

    # Function_1_3F1 end

    def Function_2_417(): pass

    label("Function_2_417")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43A")
    OP_8D(0xFE, -2480, 144940, 3210, 138830, 2000)
    Jump("Function_2_417")

    label("loc_43A")

    Return()

    # Function_2_417 end

    def Function_3_43B(): pass

    label("Function_3_43B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_448")
    Jump("loc_626")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_578")

    ChrTalk(    #0
        0xFE,
        "*sigh* Duke Dunan's come back to the castle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'd be a thousand times happier taking care\x01",
            "of Colonel Richard over at the fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "...But, you know, the duke doesn't stare at\x01",
            "people with those same lecherous, dirty eyes\x01",
            "like he used to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Ah... H-Have I gotten heavier lately?\x02",
    )

    CloseMessageWindow()
    Jump("loc_626")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_626")

    ChrTalk(    #4
        0xFE,
        (
            "It's such a relief that the duke's staying\x01",
            "over in the villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "After all, the duke was always staring at people\x01",
            "with these lecherous, dirty eyes... *shudder*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_626")

    TalkEnd(0xFE)
    Return()

    # Function_3_43B end

    def Function_4_62A(): pass

    label("Function_4_62A")

    EventBegin(0x0)
    OP_6D(840, 500, 153020, 0)
    OP_67(0, 5330, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    SetChrPos(0x8, 40, 750, 155220, 180)
    SetChrPos(0x9, 1350, 500, 153580, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 610, 0, 150320, 0)
    SetChrPos(0x102, -590, 0, 150300, 0)
    SetChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x102,
        (
            "#1035F#2P...And that is the situation as it stands\x01",
            "and all the information I gathered while\x01",
            "aboard the Glorious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#163F#6PMmmm... This is like looking\x01",
            "into the maw of madness.\x02\x03",

            "To think a monster of a ship like\x01",
            "that has intruded into Liberl...\x02\x03",

            "#166FWhat could they possibly plan to\x01",
            "do with something so powerful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1043F#2PUnfortunately, I did not manage to learn\x01",
            "all the details of the Gospel Plan.\x02\x03",

            "#1042FI do know that they've already begun\x01",
            "the next phase of it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1015F#2PThey said the 'third stage' of\x01",
            "the plan was getting ready\x01",
            "to start, but that's about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#094F#6PThe situation is grim...\x02\x03",

            "#093FGeneral Morgan. Has the army\x01",
            "begun to plan a response?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    Sleep(500)

    ChrTalk(    #11
        0x9,
        (
            "#165F#4PThese two, as might be expected, contacted\x01",
            "Cassius last night before coming to us.\x02\x03",

            "At his suggestion, I've put the entire\x01",
            "army on a state of high alert.\x02\x03",

            "We have the entire aerial fleet in the\x01",
            "air patrolling the width and breadth\x01",
            "of the kingdom now, Your Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "#090F#6PI see. Very good.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(    #13
        0x8,
        (
            "#090FEstelle, Joshua.\x01",
            "Thank you very much for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1016F#2PN-No, it's nothing!\x01",
            "We just did the right thing, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#1043F#2PTo be honest... I should have\x01",
            "approached you much earlier.\x02\x03",

            "I apologize for my earlier behavior,\x01",
            "especially the theft of the airship.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #16
        0x101,
        "#1020F#2PWait, Joshua...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #17
        0x102,
        (
            "#1054F#5PIt's all right, Estelle.\x02\x03",

            "#1053FI'm prepared for whatever\x01",
            "punishment they deem fit.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    Sleep(500)

    ChrTalk(    #18
        0x9,
        (
            "#166F#4PHmmmm... Your Majesty,\x01",
            "what shall we do with him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#094F#6PYes... I believe we will have to\x01",
            "bend the letter of the law to\x01",
            "match its spirit, in this case.\x02\x03",

            "#090FIn light of all of the information on\x01",
            "the society you have brought us,\x01",
            "Joshua Astray...\x02\x03",

            "I am willing to pardon you\x01",
            "for your past deeds.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DCF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DCF)
    Sleep(100)
    OP_8C(0x102, 0, 400)

    ChrTalk(    #20
        0x101,
        "#1018F#2PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#1042F#2PBut, Your Ma--\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrPos(0x8, 10, 500, 154550, 180)
    SetChrChipByIndex(0x8, 12)
    SetChrSubChip(0x8, 0)
    OP_0D()

    def lambda_E43():
        OP_6D(840, 500, 152500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E43)

    def lambda_E5B():
        OP_8F(0xFE, 0xFFFFFFF6, 0x1F4, 0x25328, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E5B)
    Sleep(500)

    def lambda_E7B():

        label("loc_E7B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E7B")

    QueueWorkItem2(0x9, 1, lambda_E7B)
    WaitChrThread(0x8, 0x1)
    OP_44(0x9, 0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #22
        0x8,
        (
            "#090F#6PIt is all right, Joshua.\x02\x03",

            "#094FTo be honest...an orphan of Hamel\x01",
            "deserves a far greater recompense\x01",
            "than a queen's simple discretion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1004F#2POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1043F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#094F#6P...As I imagined, you do know.\x02\x03",

            "#093FThat I knew of the massacre, and have\x01",
            "remained quiet about it until now...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x101,
        (
            "#1020F#2PWhaa?!\x02\x03",

            "What do you mean?!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, -180, 400)
    Sleep(500)

    ChrTalk(    #27
        0x9,
        (
            "#166F#6PThe Hundred Days War began with\x01",
            "a furious declaration of war from\x01",
            "Erebonia to Liberl.\x02\x03",

            "It was given on the basis that the...\x01",
            "butchery at Hamel was conducted\x01",
            "by Liberl's armed forces.\x02\x03",

            "#163FHowever, as a condition of the treaty that ended\x01",
            "the war, the Empire retracted the accusation...\x02\x03",

            "#160F...on the grounds that neither side\x01",
            "would ever, under any circumstances,\x01",
            "speak of Hamel again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1020F#2P#3SJust like Loewe said...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#094F#6POnce I considered the circumstances, I could,\x01",
            "if vaguely, see what had happened in the Empire.\x02\x03",

            "#093FHowever, even though Cassius' counter-attack\x01",
            "plan had gained us significant victories,\x01",
            "Erebonia had not committed the bulk of...\x02\x03",

            "...its military to the invasion of Liberl.\x01",
            "If they returned, with the greater part of\x01",
            "their army...\x02\x03",

            "#094FAfter realizing that, I agreed\x01",
            "to their conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1026F#2POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1043F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#092F#6PI chose to prioritize my nation's\x01",
            "safety over the pursuit of the\x01",
            "truth.\x02\x03",

            "I destroyed any hope the victims,\x01",
            "who were lost in the shadows,\x01",
            "had for justice.\x02\x03",

            "#094FThose words that Lt. Lorence...that\x01",
            "Leonhardt said to me. 'You are hardly\x01",
            "qualified to feel pity for me.'\x02\x03",

            "He was absolutely correct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1026F#2PYour Majesty...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#1035F#2PYour Majesty, please.\x01",
            "Do not blame yourself.\x02\x03",

            "#1040FYou had no connection to the\x01",
            "massacre, and the safety of\x01",
            "your entire nation was at risk.\x02\x03",

            "As a ruler, you made the right decision.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #35
        0x8,
        "#093F#6PJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#1053F#2PThis land of Liberl is my home. It is the\x01",
            "place that mended my broken heart.\x02\x03",

            "#1040FI don't hate you for choosing to protect\x01",
            "it, Your Majesty--I thank you for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1025F#2PJoshua! Yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#096F#6PThank you, Joshua.\x02\x03",

            "To hear you say that feels as though\x01",
            "a burden was lifted from my shoulders.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, 520, 0, 138480, 0)
    SetChrPos(0xE, -850, 0, 138320, 0)
    SetChrPos(0xA, -2560, 0, 137730, 0)
    SetChrPos(0xD, -2280, 0, 136550, 0)
    SetChrPos(0xB, 1570, 0, 138000, 0)
    SetChrPos(0xF, 2440, 0, 137650, 0)
    Sleep(500)

    NpcTalk(    #39
        0xC,
        "Girl's Voice",
        "#1PEstelle! Joshua!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_17CE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17CE)
    Sleep(100)
    OP_8C(0x102, 180, 400)

    ChrTalk(    #40
        0x101,
        "#1004F#5PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#1044F#5PEveryone...\x02",
    )

    CloseMessageWindow()

    def lambda_1814():
        OP_6D(1130, 0, 150940, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1814)

    def lambda_182C():
        OP_67(0, 5380, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_182C)

    def lambda_1844():
        OP_6B(2770, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1844)

    def lambda_1854():
        OP_6E(344, 2000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1854)
    OP_43(0xC, 0x0, 0x0, 0x6)
    Sleep(300)
    OP_43(0xE, 0x0, 0x0, 0x7)
    Sleep(300)
    OP_43(0xA, 0x0, 0x0, 0x8)
    Sleep(300)
    OP_43(0xD, 0x0, 0x0, 0x9)
    Sleep(300)
    OP_43(0xB, 0x0, 0x0, 0xA)
    Sleep(300)
    OP_43(0xF, 0x0, 0x0, 0xB)
    WaitChrThread(0xC, 0x0)
    Sleep(500)

    NpcTalk(    #42
        0xC,
        "Kloe",
        (
            "#041F#2PEstelle! I'm so glad you're safe!\x02\x03",

            "#048FAnd...Joshua...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x0)

    ChrTalk(    #43
        0xE,
        (
            "#067F#2PYou're both back!\x01",
            "You're both baaaaack!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        "#1054F#6PKloe, Tita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1025F#6PHi, guys...\x01",
            "Sorry to make you worry.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x0)

    ChrTalk(    #46
        0xA,
        (
            "#027F#5PReally, you two. The way you\x01",
            "behave can drive a woman\x01",
            "to drink, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        (
            "#051F#5PHeh...\x02\x03",

            "Still, though, good to see you brought\x01",
            "back our little runaway after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#1040F#6PSchera, Agate...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF, 0x0)

    ChrTalk(    #49
        0xF,
        "#070F#2PGlad to see you two are back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        (
            "#031F#4PHeh, I am certain this, too,\x01",
            "must be the divine guidance\x01",
            "of Aidios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1016F#6PAhaha... Sorry for all the fuss.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, 40, 0, 140750, 0)

    NpcTalk(    #52
        0x10,
        "Young Man's Voice",
        "#1PYa dang well better be!\x02",
    )

    CloseMessageWindow()

    def lambda_1B51():
        OP_6D(1130, 0, 150500, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1B51)

    def lambda_1B69():

        label("loc_1B69")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1B69")

    QueueWorkItem2(0xB, 1, lambda_1B69)

    def lambda_1B7A():

        label("loc_1B7A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1B7A")

    QueueWorkItem2(0xF, 1, lambda_1B7A)
    Sleep(50)

    def lambda_1B90():

        label("loc_1B90")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1B90")

    QueueWorkItem2(0xA, 1, lambda_1B90)

    def lambda_1BA1():

        label("loc_1BA1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1BA1")

    QueueWorkItem2(0xD, 1, lambda_1BA1)
    Sleep(50)

    def lambda_1BB7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1BB7)

    def lambda_1BC5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1BC5)
    Sleep(50)

    def lambda_1BD8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BD8)
    OP_8C(0x101, 180, 400)
    ClearChrFlags(0x10, 0x80)

    def lambda_1BF2():
        OP_8E(0x10, 0xFFFFFEC0, 0x0, 0x24400, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1BF2)
    Sleep(500)
    OP_43(0xC, 0x0, 0x0, 0xD)
    Sleep(100)
    OP_43(0xE, 0x0, 0x0, 0xE)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0xC, 0x0)
    WaitChrThread(0xE, 0x0)
    OP_44(0xB, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xC, 0x1)

    def lambda_1C4C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C4C)

    def lambda_1C5A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C5A)
    Sleep(50)

    def lambda_1C6D():

        label("loc_1C6D")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_1C6D")

    QueueWorkItem2(0xA, 1, lambda_1C6D)

    def lambda_1C7E():

        label("loc_1C7E")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_1C7E")

    QueueWorkItem2(0xD, 1, lambda_1C7E)
    Sleep(50)

    def lambda_1C94():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C94)

    def lambda_1CA2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1CA2)

    ChrTalk(    #53
        0x101,
        "#1004F#6POh, Kevin!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #54
        0x10,
        (
            "#1068F#2PI gotta tell ya, Estelle, when you\x01",
            "got snatched up I just about flipped\x01",
            "out in every direction I could.\x02\x03",

            "#1060FSeriously, don't make me worry\x01",
            "like that next time, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1025F#6PYeah... Sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        "#1062F#2PSo, then! THIS must be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#1040F#6PYes, I'm Joshua Astray.\x01",
            "A pleasure to meet you, Father Graham.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#1068F#2PUrk. Even more handsome\x01",
            "than I'd expected.\x02\x03",

            "#1064FAnd, wait, you know me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#1053F#6PI heard about you once or twice\x01",
            "while keeping an ear open for\x01",
            "what Estelle was doing.\x02\x03",

            "I heard how you helped Estelle when\x01",
            "she was in need several times.\x02\x03",

            "#1040FThank you. I'm grateful for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#1065F#2PMmmmmm... Eh, it wasn't a big deal.\x02\x03",

            "#1060FSo if you two have made up,\x01",
            "I won't say anything.\x02\x03",

            "#1063FExcept...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FCC():
        OP_6D(840, 0, 151500, 1200)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1FCC)

    def lambda_1FE4():
        OP_6B(2700, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FE4)

    def lambda_1FF4():

        label("loc_1FF4")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1FF4")

    QueueWorkItem2(0x101, 1, lambda_1FF4)

    def lambda_2005():

        label("loc_2005")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2005")

    QueueWorkItem2(0xC, 1, lambda_2005)

    def lambda_2016():

        label("loc_2016")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2016")

    QueueWorkItem2(0xF, 1, lambda_2016)
    SetChrFlags(0x10, 0x40)
    OP_8F(0x10, 0xFFFFFBF0, 0x0, 0x24856, 0x5DC, 0x0)
    OP_8C(0x10, 0, 400)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)

    def lambda_204F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_204F)
    Sleep(100)
    OP_8C(0x101, 270, 400)
    Sleep(500)

    ChrTalk(    #61
        0x10,
        (
            "#1066F#4P(Just don't leave your girlfriend\x01",
            "in the lurch like that again, eh?)\x02\x03",

            "(Otherwise some of us'll take\x01",
            "that as a cue she's single again!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        "#1054F#3P(...I will, uh, keep that in mind.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1004F#4PHuh? What're you two\x01",
            "whispering about?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 400)

    ChrTalk(    #64
        0x10,
        "#1061F#6PNothin', just a 'guy thing'.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #65
        0x102,
        "#1049F#3PYes, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1019F#4PIf it's something dirty, I can show you\x01",
            "the 'Girl Thing We Do With A Stick' in\x01",
            "response.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xF, 0x1)
    Sleep(500)
    SetChrPos(0x11, 40, 0, 140750, 0)

    NpcTalk(    #67
        0x11,
        "Man's Voice",
        "#1PPardon me, Your Majesty.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    ClearChrFlags(0x11, 0x80)
    Sleep(1000)

    def lambda_22B7():

        label("loc_22B7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_22B7")

    QueueWorkItem2(0xB, 1, lambda_22B7)

    def lambda_22C8():

        label("loc_22C8")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_22C8")

    QueueWorkItem2(0xF, 1, lambda_22C8)
    Sleep(50)

    def lambda_22DE():

        label("loc_22DE")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_22DE")

    QueueWorkItem2(0xA, 1, lambda_22DE)

    def lambda_22EF():

        label("loc_22EF")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_22EF")

    QueueWorkItem2(0xD, 1, lambda_22EF)
    Sleep(50)

    def lambda_2305():

        label("loc_2305")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_2305")

    QueueWorkItem2(0xE, 1, lambda_2305)

    def lambda_2316():

        label("loc_2316")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_2316")

    QueueWorkItem2(0xC, 1, lambda_2316)
    Sleep(50)

    def lambda_232C():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_232C)

    def lambda_233A():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_233A)
    Sleep(50)
    TurnDirection(0x101, 0x11, 400)

    def lambda_2354():
        OP_6D(960, 0, 151060, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2354)

    def lambda_236C():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_236C)

    def lambda_237C():
        OP_8E(0x11, 0xFFFFFD1C, 0x0, 0x23A50, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_237C)
    WaitChrThread(0x10, 0x1)
    Sleep(1000)
    OP_43(0x10, 0x0, 0x0, 0xC)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #68
        0x101,
        "#1025F#6PDad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        "#1044F#6PCassius...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        "#090F#6PGeneral Bright, thank you for coming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#165F#6PHave you gotten the orders\x01",
            "out to all forces?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x11,
        (
            "#1125F#2PYes. I flew out here as\x01",
            "soon as I was finished.\x02\x03",

            "#1120FI thought it was about time to\x01",
            "come and do my duty as a father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1004F#6PWha?\x02",
    )

    CloseMessageWindow()

    def lambda_24DF():
        OP_6D(1130, 0, 151500, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_24DF)

    def lambda_24F7():

        label("loc_24F7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_24F7")

    QueueWorkItem2(0x101, 1, lambda_24F7)
    OP_8E(0x11, 0xFFFFFE3E, 0x0, 0x2489C, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(    #74
        0x11,
        (
            "#1120F#4PWe spoke on the phone yesterday,\x01",
            "but this is the first time we've met\x01",
            "face to face in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#1035F#6PYes...it is.\x02\x03",

            "#1043FI'm sorry I made you worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x11,
        (
            "#1125F#4PI knew the oath you made. I'm nearly\x01",
            "as much to blame as you are.\x02\x03",

            "#1122FYou needn't apologize, but...\x01",
            "I must do my duty.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_2659():
        OP_6B(2600, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2659)
    Sleep(600)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    Fade(500)
    SetChrPos(0x11, -580, 0, 150280, 0)
    SetChrPos(0x18, -450, 0, 149780, 0)
    SetChrPos(0x102, -590, 0, 150200, 180)
    SetChrFlags(0x11, 0x2)
    SetChrSubChip(0x11, 24)
    SetChrChipByIndex(0x11, 13)
    SetChrFlags(0x102, 0x2)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 13)
    SetChrFlags(0x102, 0x40)
    OP_0D()

    def lambda_26E6():
        OP_99(0x102, 0x0, 0xA, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_26E6)

    def lambda_26F6():
        OP_99(0x11, 0x18, 0x27, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_26F6)
    Sleep(300)
    OP_22(0xA5, 0x0, 0x64)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #77
        0xE,
        "#065F#1PAh!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #78
        0xC,
        "Kloe",
        "#043F#4POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1020F#7PWhoa! Wait, DAD!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        "#1035F#6PIt's all right, Estelle.\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0xB, 0xF, 0x5DC)
    Sleep(500)

    ChrTalk(    #81
        0x102,
        (
            "#1040F#6PThat's what you're supposed to\x01",
            "do to a runaway son, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x18,
        "Cassius",
        (
            "#1125F#4PExactly.\x02\x03",

            "#1120FIt looks like you understand now...\x02\x03",

            "...just how badly everyone\x01",
            "was worried about you, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#1043F#6P...Yes.\x02\x03",

            "#1035FIt's just the sort of thing someone\x01",
            "like me wouldn't realize, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x18,
        "Cassius",
        (
            "#1122F#4PYes, it is a hard thing to truly grasp.\x02\x03",

            "#1125FNo man stands alone, even if\x01",
            "he tries his hardest to. He is\x01",
            "affected by those around him.\x02\x03",

            "And conversely, he affects those around\x01",
            "him, simply through the act of living.\x02\x03",

            "Even without meaning to, we form relationships.\x01",
            "And in time, those relationships become bonds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        "#1044F#6PBonds...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #86
        0x18,
        "Cassius",
        (
            "#1120F#4PAnd a bond, once formed, never breaks.\x02\x03",

            "No matter how far we travel, no matter what\x01",
            "path we follow...they remain in some form.\x02\x03",

            "#1121FDo you understand just how strong\x01",
            "such bonds can be, now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#1054F#6PYes...\x01",
            "Honestly, I'd underestimated them.\x02\x03",

            "#1053FI didn't understand how powerful\x01",
            "they could be at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1025F#7PJoshua...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #89
        0x18,
        "Cassius",
        (
            "#1120F#4PIf you've learned that, then I think your\x01",
            "little walking tour was worth it.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x11, -580, 0, 150130, 0)
    SetChrPos(0x18, -530, 0, 149780, 0)

    def lambda_2C1A():
        OP_99(0x102, 0x10, 0x14, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2C1A)

    def lambda_2C2A():
        OP_99(0x11, 0x28, 0x2C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2C2A)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(1000)

    NpcTalk(    #90
        0x18,
        "Cassius",
        (
            "#1125F#4PJoshua...you damn fool\x01",
            "of a son of mine.\x02\x03",

            "Welcome home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        "#1043F#6PCassius... Dad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1008F#7P*sniffle* Heehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "#165F#6PHmph, I might say half the foolishness\x01",
            "comes from the parent myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#091F#6PIt's a lovely moment,\x01",
            "Morgan. Come now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x12, -40, 0, 138750, 0)

    NpcTalk(    #95
        0x12,
        "Woman's Voice",
        "#1PPardon me!\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2EC4():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2EC4)

    def lambda_2ED4():

        label("loc_2ED4")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2ED4")

    QueueWorkItem2(0xB, 1, lambda_2ED4)

    def lambda_2EE5():

        label("loc_2EE5")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2EE5")

    QueueWorkItem2(0xF, 1, lambda_2EE5)
    Sleep(50)

    def lambda_2EFB():

        label("loc_2EFB")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2EFB")

    QueueWorkItem2(0xA, 1, lambda_2EFB)

    def lambda_2F0C():

        label("loc_2F0C")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2F0C")

    QueueWorkItem2(0xD, 1, lambda_2F0C)
    Sleep(50)

    def lambda_2F22():

        label("loc_2F22")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2F22")

    QueueWorkItem2(0xC, 1, lambda_2F22)

    def lambda_2F33():

        label("loc_2F33")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2F33")

    QueueWorkItem2(0xE, 1, lambda_2F33)
    Sleep(50)

    def lambda_2F49():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F49)

    def lambda_2F57():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2F57)
    Fade(250)
    OP_43(0x11, 0x1, 0x0, 0x5)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()

    def lambda_2F81():
        OP_6D(1390, 0, 150800, 1500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2F81)
    ClearChrFlags(0x12, 0x80)
    OP_8E(0x12, 0xFFFFFE3E, 0x0, 0x23E38, 0xFA0, 0x0)
    OP_44(0x102, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xA, 0x1)

    ChrTalk(    #96
        0x8,
        "#097F#6PCaptain Schwarz? What is it?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x23)
    Sleep(500)

    ChrTalk(    #97
        0x12,
        (
            "#172F#2PYour Majesty! Sirs! There are massive\x01",
            "groups of unidentified...CREATURES\x01",
            "near all five major cities!\x02\x03",

            "From the reports, we suspect they\x01",
            "may be archaisms, but we're not sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1005F#6PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        "#1042F#6PThey've started moving.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x12,
        (
            "#172F#2PAlso, we've received reports of herds\x01",
            "of armored beasts and soldiers\x01",
            "wearing red from every region!\x02\x03",

            "Local guard forces are engaged\x01",
            "in fighting them back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        "#1125F#5PAs I feared.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "#160F#6PI should return to\x01",
            "Haken Gate immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x12,
        "#175FAlso...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        "#161F#6PSchwarz, there can't possibly be MORE.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x12,
        (
            "#178FThere is. We lack details, but there\x01",
            "is some kind of...'abnormality,' is\x01",
            "the only way to put it, at the towers.\x02\x03",

            "The top of each tower has been...\x01",
            "engulfed in darkness. It's bizarre.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1020F#6PWhat in the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "#1063F#6PI hate it when my bad feelings\x01",
            "turn out to be right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x12,
        (
            "#178FFurthermore, a guard ship on patrol\x01",
            "attempted to approach one...\x02\x03",

            "But it began suffering catastrophic\x01",
            "system failure as it approached and\x01",
            "only barely managed to pull back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        "#160F#6POrbal suspension.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x11,
        "#1122F#5PWhat about ground-based scouts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x12,
        (
            "#175FI've already dispatched them.\x01",
            "No word back y--\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x13, 70, 0, 136750, 0)
    ClearChrFlags(0x13, 0x80)

    NpcTalk(    #112
        0x13,
        "Man's Voice",
        (
            "#1PE-Excuse me! Captain Schwarz!\x01",
            "I have a report!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3629():
        OP_6D(1350, 0, 150430, 1500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3629)

    def lambda_3641():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3641)

    def lambda_3651():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3651)

    def lambda_365F():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_365F)
    Sleep(50)

    def lambda_3672():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3672)

    def lambda_3680():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3680)
    Sleep(50)

    def lambda_3693():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3693)

    def lambda_36A1():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_36A1)
    Sleep(50)

    def lambda_36B4():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36B4)

    def lambda_36C2():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_36C2)

    def lambda_36D0():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_36D0)
    OP_8E(0x13, 0xFFFFFF38, 0x0, 0x23668, 0xFA0, 0x0)

    ChrTalk(    #113
        0x13,
        (
            "#2PThe scouting units deployed to the\x01",
            "towers have all been destroyed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x13,
        (
            "#2PIt sounds impossible, but every squad\x01",
            "was scattered by just one person!\x01",
            "The reports are consistent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x12,
        "#173F#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1005F#6PThat can only be...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#1035F#6PYes. Only an Enforcer could do that.\x02\x03",

            "#1042FDad. The normal army troops\x01",
            "have no hope of defeating them.\x02\x03",

            "Let me go.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3864():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3864)

    def lambda_3872():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3872)
    Sleep(50)

    def lambda_3885():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3885)

    def lambda_3893():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3893)
    Sleep(50)

    def lambda_38A6():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_38A6)

    def lambda_38B4():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_38B4)
    Sleep(50)

    def lambda_38C7():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_38C7)

    def lambda_38D5():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_38D5)
    Sleep(50)

    def lambda_38E8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38E8)
    TurnDirection(0x12, 0x102, 400)
    Sleep(200)

    ChrTalk(    #118
        0x11,
        "#1125F#4PHm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1009F#4PExcuse me, Joshua...but why are\x01",
            "you trying to go out on your own?\x02\x03",

            "Did you already forget the promise we made?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #120
        0x102,
        "#1043F#6PBut, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1006F#4PThe society's on the move.\x01",
            "As a bracer of Liberl, I can't\x01",
            "just sit back and ignore them!\x02\x03",

            "I'm going after them too.\x01",
            "Either way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x102,
        "#1044F#6PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        (
            "#020F#5PIt isn't just Estelle, either.\x01",
            "I'm coming as well.\x02\x03",

            "I have my own personal reasons for wanting\x01",
            "to confront one of them, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xF,
        "#070FAs do I.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)
    Sleep(500)

    ChrTalk(    #125
        0x102,
        "#1044F#6PSchera, Zin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xD,
        (
            "#051F#2PPoint is, you ain't the only\x01",
            "one tied up in this.\x02\x03",

            "No runnin' off without us, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xE,
        (
            "#560F#5PThat's right, Joshua!\x02\x03",

            "#061FThis is just the kind of time\x01",
            "we all need to work together!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)
    Sleep(500)

    ChrTalk(    #128
        0x102,
        (
            "#1054F#6PAgate. Tita...\x02\x03",

            "#1053F...Thank you. I appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x11,
        (
            "#1125F#4PLooks like you've decided.\x02\x03",

            "#1122FThen allow me to make a formal\x01",
            "request of the Bracer Guild on\x01",
            "behalf of the Royal Army.\x02\x03",

            "I want you to investigate and\x01",
            "resolve the situations at each\x01",
            "of the Tetracyclic Towers.\x02\x03",

            "Bring the phenomena to a halt, and,\x01",
            "if possible, apprehend those responsible.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    def lambda_3D77():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D77)
    Sleep(500)

    ChrTalk(    #130
        0x101,
        "#1006F#6PYeah... Got it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        (
            "#1042F#6PThe guild accepts your mission,\x01",
            "General Bright.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xC)
    OP_8C(0xC, 0, 400)
    Sleep(500)

    NpcTalk(    #132
        0xC,
        "Kloe",
        (
            "#042F#4PGrandmother...\x02\x03",

            "Will you lend us the Arseille?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #133
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xC, 400)

    def lambda_3E6E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3E6E)

    def lambda_3E7C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E7C)

    ChrTalk(    #134
        0x12,
        "#173F#2PY-Your Highness?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x8,
        (
            "#094F#6PCertainly. This is a situation\x01",
            "which demands haste.\x02\x03",

            "I was considering offering the\x01",
            "Arseille regardless, but...\x02\x03",

            "#090FIf you are asking yourself, does\x01",
            "that mean you are ready?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #136
        0xC,
        "Kloe",
        (
            "#049F#4PNo... Not yet.\x02\x03",

            "#042FWhen I return the ship, however,\x01",
            "then I will have an answer for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "#090F#6PHeehee. Very well.\x02\x03",

            "#091FLiberl's wings of hope are\x01",
            "yours to use as you see fit.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #138
        0xC,
        "Kloe",
        "#048F#4PThank you very much.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x12, 400)
    Sleep(500)

    NpcTalk(    #139
        0xC,
        "Kloe",
        (
            "#042F#6PJulia! Prepare the Arseille\x01",
            "for launch, please.\x02\x03",

            "We must head to the\x01",
            "towers immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x12,
        "#171F#2PBy your command, milady!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #141
        (
            "\x07\x05And so Liberl fell into chaos not seen since the\x01",
            "Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #142
        (
            "\x07\x05Cassius and Morgan returned to Leiston Fortress and the\x01",
            "Haken Gate, respectively, to take command of the Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #143
        (
            "\x07\x05Meanwhile, Estelle and her friends headed for the towers\x01",
            "which dotted the landscape using the Arseille.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x98, 0x4, 0x10)
    OP_AF(0xCD, 0x98)
    Sleep(100)
    OP_28(0x99, 0x4, 0x10)
    OP_28(0x99, 0x4, 0x20)
    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_62A end

    def Function_5_4276(): pass

    label("Function_5_4276")

    SetChrPos(0x11, -450, 0, 149660, 0)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x800)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x24540, 0x3E8, 0x0)
    Return()

    # Function_5_4276 end

    def Function_6_42BC(): pass

    label("Function_6_42BC")

    SetChrChipByIndex(0xFE, 15)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xB4, 0x0, 0x242AC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 4)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_42BC end

    def Function_7_42E7(): pass

    label("Function_7_42E7")

    SetChrChipByIndex(0xFE, 16)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFC68, 0x0, 0x24284, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 6)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_7_42E7 end

    def Function_8_4312(): pass

    label("Function_8_4312")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF560, 0x0, 0x2457C, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_8_4312 end

    def Function_9_4333(): pass

    label("Function_9_4333")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF5B0, 0x0, 0x23F46, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_9_4333 end

    def Function_10_4354(): pass

    label("Function_10_4354")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x8FC, 0x0, 0x24662, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_10_4354 end

    def Function_11_4375(): pass

    label("Function_11_4375")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x398, 0x0, 0x23FA0, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_4375 end

    def Function_12_4396(): pass

    label("Function_12_4396")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0x24C70, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_12_4396 end

    def Function_13_43B7(): pass

    label("Function_13_43B7")

    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0x384, 0x0, 0x2446E, 0x3E8, 0x0)

    def lambda_43D6():

        label("loc_43D6")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_43D6")

    QueueWorkItem2(0xFE, 1, lambda_43D6)
    Return()

    # Function_13_43B7 end

    def Function_14_43E2(): pass

    label("Function_14_43E2")

    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFFF844, 0x0, 0x24432, 0x3E8, 0x0)

    def lambda_4401():

        label("loc_4401")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4401")

    QueueWorkItem2(0xFE, 1, lambda_4401)
    Return()

    # Function_14_43E2 end

    def Function_15_440D(): pass

    label("Function_15_440D")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(830, 0, 138280, 0)
    OP_67(0, 8039, -10000, 0)
    OP_6B(2350, 0)
    OP_6C(44000, 0)
    OP_6E(488, 0)
    OP_D2(0x70141, 0x70145, 0x12)
    OP_D2(0x6011B, 0x60120, 0x13)
    OP_D2(0x2701D4, 0x2701D9, 0x14)
    OP_D2(0x2700B0, 0x2700B4, 0x15)
    OP_D2(0x700E0, 0x700E4, 0x16)
    OP_D2(0x704AA, 0x704AE, 0x17)
    SetChrChipByIndex(0x8, 18)
    SetChrChipByIndex(0xC, 19)
    SetChrChipByIndex(0x15, 20)
    SetChrChipByIndex(0x16, 21)
    SetChrChipByIndex(0x17, 22)
    SetChrChipByIndex(0x14, 23)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -90, 0, 150140, 180)
    SetChrPos(0x14, 3790, 800, 152270, 270)
    SetChrPos(0xC, -1510, 0, 148970, 180)
    SetChrPos(0x15, 1650, 0, 148500, 180)
    SetChrPos(0x16, 560, 0, 148300, 180)
    SetChrPos(0x101, -360, 0, 145930, 0)
    SetChrPos(0x102, 790, 0, 145890, 0)
    SetChrPos(0xA, 740, 0, 144730, 0)
    SetChrPos(0xD, -800, 0, 143680, 0)
    SetChrPos(0xE, -1250, 0, 144610, 0)
    SetChrPos(0xF, 1230, 0, 143850, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x14, 0x80)
    FadeToBright(1000, 0)

    def lambda_45C0():
        OP_6D(290, 0, 147230, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45C0)

    def lambda_45D8():
        OP_67(0, 7500, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_45D8)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(1500, 0, 147770, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(44000, 0)
    OP_6E(433, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #144
        0x15,
        (
            "#700F#6PAs I mentioned previously, I'm here\x01",
            "on General Bright's orders.\x02\x03",

            "He had a suspicion that Ouroboros\x01",
            "might try something like this.\x02\x03",

            "#703FHowever, most regular army troops aren't\x01",
            "very well trained to fight without their\x01",
            "orbal firearms...\x02\x03",

            "#701FSo he decided to use a handful of troops\x01",
            "with experience in hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x16,
        (
            "#115F#6POf course, he needed an excuse to get\x01",
            "me and my subordinates involved, seeing\x01",
            "as we are supposed to be in prison.\x02\x03",

            "#111FAs a result, we were to be transported to\x01",
            "Grancel, where we conveniently ended up\x01",
            "caught in the chaos and repelled the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1007F#2POooookay...\x02\x03",

            "#1019FThat's about as subtle as a\x01",
            "brick to the forehead, Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        (
            "#1040F#4PI take it you had some idea about\x01",
            "this, Your Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#090F#6PYes, Cassius and I discussed the idea earlier.\x02\x03",

            "We will, I suspect, face some criticism for\x01",
            "doing this, but the safety of the citizenry\x01",
            "must come before everything else.\x02\x03",

            "#091FAnd I knew, from the bottom of my heart,\x01",
            "that Mr. Richard would do what was best\x01",
            "for the country he loves so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x16,
        (
            "#115F#6PI do not deserve such praise,\x01",
            "Your Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1006F#2PI get it. So then...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #151
        0x101,
        (
            "#1015F#2POh, uh, right.\x02\x03",

            "Does this have to do with the\x01",
            "reason you wanted to see us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        (
            "#094F#6PIn part, yes.\x02\x03",

            "#090FWhat I wanted to discuss was\x01",
            "what Klaudia has done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1004F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x102,
        "#1044F#4PWhat Kloe's done?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xC,
        (
            "#406F#6PYes...\x02\x03",

            "#400FIt was a short ceremony, but as of this morning,\x01",
            "I've been formally invested with the inheritance.\x02\x03",

            "I am now, officially, the crown princess of\x01",
            "Liberl, next in line to be queen.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #156
        0x101,
        "#1004F#2PWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xE,
        "#560F#2PWow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x102,
        (
            "#1040F#4PCongratulations.\x01",
            "I think you made a good decision.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E47")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as cleared the quest to free the academy\x01",            # 0
            "Set as did not clear the quest to free the academy\x01",      # 1
            "No change\x01",                                               # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4E3B"),
        (1, "loc_4E41"),
        (SWITCH_DEFAULT, "loc_4E47"),
    )


    label("loc_4E3B")

    OP_A2(0x202F)
    Jump("loc_4E47")

    label("loc_4E41")

    OP_A3(0x202F)
    Jump("loc_4E47")

    label("loc_4E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_506F")

    ChrTalk(    #159
        0xC,
        (
            "#466F#6PI...really think some of it is simply\x01",
            "selfishness on my part.\x02\x03",

            "#405FEstelle, everyone...\x02\x03",

            "I understand you're the ones who\x01",
            "saved everyone at the academy?\x02\x03",

            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#1016F#2POh! Uh, yeah.\x02\x03",

            "#1006FWe can't really take\x01",
            "all the credit, though.\x02\x03",

            "Anelace's group was there,\x01",
            "and Sieg helped out too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x14,
        "#311F#6PScreee. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xC,
        (
            "#401F#6PHaha! Yes, so I gathered.\x02\x03",

            "#406FWhen I learned about what happened...\x01",
            "I spent a lot of time thinking about what\x01",
            "I could do.\x02\x03",

            "What role I could serve to help\x01",
            "protect those dear to me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5158")

    label("loc_506F")


    ChrTalk(    #163
        0xC,
        (
            "#405F#6PI...really think some of it is simply\x01",
            "selfishness on my part.\x02\x03",

            "#406FThe entire kingdom is in chaos...\x01",
            "I've spent a lot of time thinking\x01",
            "about what I could do.\x02\x03",

            "What role I could serve to help\x01",
            "protect those dear to me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5158")


    ChrTalk(    #164
        0x102,
        "#1040F#4PAnd that's inheriting the throne?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xC,
        (
            "#400F#6PYes.\x02\x03",

            "#406FI am an inexperienced teenager who\x01",
            "lacks the ability or confidence to lead\x01",
            "an entire kingdom.\x02\x03",

            "Still, if I can use such a position\x01",
            "to protect those dear to me...\x02\x03",

            "...and if that in turn helps me\x01",
            "to protect the home I love...\x02\x03",

            "#401F...then it is all worth it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#1017F#2PKloe... You silly...\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_52D1():
        OP_6D(-40, 0, 149310, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52D1)

    def lambda_52E9():

        label("loc_52E9")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_52E9")

    QueueWorkItem2(0x8, 2, lambda_52E9)

    def lambda_52FA():

        label("loc_52FA")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_52FA")

    QueueWorkItem2(0x15, 2, lambda_52FA)

    def lambda_530B():

        label("loc_530B")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_530B")

    QueueWorkItem2(0x16, 2, lambda_530B)

    def lambda_531C():

        label("loc_531C")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_531C")

    QueueWorkItem2(0x102, 2, lambda_531C)

    def lambda_532D():

        label("loc_532D")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_532D")

    QueueWorkItem2(0xA, 2, lambda_532D)

    def lambda_533E():

        label("loc_533E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_533E")

    QueueWorkItem2(0xD, 2, lambda_533E)

    def lambda_534F():

        label("loc_534F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_534F")

    QueueWorkItem2(0xE, 2, lambda_534F)

    def lambda_5360():

        label("loc_5360")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5360")

    QueueWorkItem2(0xF, 2, lambda_5360)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xFFFFFABA, 0x0, 0x2437E, 0x5DC, 0x0)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xC, 0)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0x101, 0x800)
    SetChrChipByIndex(0x101, 14)
    SetChrSubChip(0x101, 16)
    SetChrFlags(0x101, 0x2)

    def lambda_53AD():
        OP_99(0x101, 0x10, 0x13, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_53AD)
    OP_99(0xC, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #167
        0x101,
        (
            "#1001F#4PWell, congratulations!\x02\x03",

            "#1018FLooks like you finally found that\x01",
            "path you were looking for, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xC, 0x4, 0x5, 0x5DC)
    Sleep(500)

    ChrTalk(    #168
        0xC,
        "#406F#6PEstelle...thank you.\x02",
    )

    CloseMessageWindow()
    OP_99(0xC, 0x5, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #169
        0xC,
        (
            "#405F#6PI really am desperately new at this, though,\x01",
            "and I am not quite sure what I can do.\x02\x03",

            "Will you...lend me your aid when I need it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1001F#4PWhat kinda question is that? Duh!\x02\x03",

            "#1008FI mean, heck, I'm not exactly a grizzled\x01",
            "veteran over here, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        (
            "#1049F#4PJust as you've lent us your aid,\x01",
            "time and time again...\x02\x03",

            "#1041FWhenever you need us,\x01",
            "we'll be there for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xC,
        (
            "#409F#6PEstelle, Joshua...\x02\x03",

            "#401FThank you... Thank you so much!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x2)
    OP_44(0x15, 0x2)
    OP_44(0x16, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xA, 0x2)
    OP_44(0xD, 0x2)
    OP_44(0xE, 0x2)
    OP_44(0xF, 0x2)
    OP_6D(910, 0, 149260, 1200)

    ChrTalk(    #173
        0x16,
        (
            "#115F#6P(What a complete and utter\x01",
            "fool I've been.)\x02\x03",

            "#116F(All the things I did without realizing\x01",
            "the potential of the young people who\x01",
            "will carry our future...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x15,
        "#700F#4P(Alan...)\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(300)

    ChrTalk(    #175
        0x8,
        (
            "#091F#6P(What's this, Alan?)\x02\x03",

            "#090F(You'll be carrying a good deal\x01",
            "of 'future' yourself, still, I think.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x15,
        "#701F#4P(Quite so!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x16,
        "#118F#4P(You jest, Your Majesty...)\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x17, 10, 0, 137650, 0)
    ClearChrFlags(0x17, 0x80)

    NpcTalk(    #178
        0x17,
        "Man's Voice",
        "#4S#1PColonel! I have a report!\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xF, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5908():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5908)

    def lambda_5916():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5916)
    Sleep(50)

    def lambda_5929():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5929)

    def lambda_5937():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5937)
    Sleep(50)

    def lambda_594A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_594A)

    def lambda_5958():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5958)
    Sleep(50)

    def lambda_596B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_596B)

    def lambda_5979():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5979)
    SetChrChipByIndex(0xC, 19)
    SetChrSubChip(0xC, 0)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x800)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x800)

    def lambda_59AF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59AF)

    def lambda_59BD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_59BD)

    def lambda_59CB():
        OP_6D(1100, 0, 146260, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59CB)

    def lambda_59E3():
        OP_67(0, 5630, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_59E3)

    def lambda_59FB():
        OP_6B(1900, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_59FB)

    def lambda_5A0B():
        OP_6E(488, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5A0B)
    Sleep(1000)

    def lambda_5A20():
        OP_8E(0xFE, 0x154, 0x0, 0x229D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5A20)
    Sleep(1000)

    def lambda_5A40():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x23A0A, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A40)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #179
        0x15,
        (
            "#702F#6PWhat is it?\x01",
            "Is the city under attack again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x17,
        "#2PN-No, sir, everything is quiet here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x17,
        (
            "#2PThe jaegers withdrew rapidly from the city\x01",
            "and faded back out into the countryside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x15,
        "#700F#6PThen what is it, man? Speak up.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    Sleep(100)
    OP_1D(0x23)
    Sleep(500)

    ChrTalk(    #183
        0x17,
        "#2PWe, we've received a report from Haken Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x17,
        "#2PAn Erebonian army is gathering at the border!\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #185
        0x101,
        "#1020F#6P#4SWhat?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #186
        0x16,
        "#117F#6PSo they've come at last...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        "#092F#6PHow large an army are they fielding?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x17,
        (
            "#2PSo far, it appears to only be\x01",
            "a single standard division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x17,
        "#2PBut they...they have tanks with them!\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #190
        0x15,
        "#704F#6PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xD,
        (
            "#055F#5PNow just a damn second!\x02\x03",

            "How the hell are they runnin'\x01",
            "TANKS in the middle of all this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xA,
        (
            "#024F#6PAre they using the same technology\x01",
            "as the society?! I thought they might...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x17,
        (
            "#2PNo, it's...strange. They don't appear\x01",
            "to be using orbments at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x17,
        (
            "#2PThe scout reports say they run\x01",
            "using steam engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#1026F#6PSteam what now?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 45, 400)
    Sleep(300)

    ChrTalk(    #196
        0xE,
        (
            "#065F#5PUm, it's an engine that uses steam\x01",
            "to move the pistons. It's even more\x01",
            "primitive than a gasoline engine...\x02\x03",

            "Everyone stopped using them as\x01",
            "soon as orbments were invented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x16,
        (
            "#112F#6PNo sane army would bother keeping\x01",
            "such museum pieces maintained.\x02\x03",

            "They're a joke compared to\x01",
            "even the most basic orbal tank.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6188():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6188)

    ChrTalk(    #198
        0xF,
        (
            "#074F#6PWhich can only mean one thing.\x02\x03",

            "#072FThey prepared these in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1002F#6PHang on. You mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x15,
        (
            "#703F#6PIt means the Erebonian leadership\x01",
            "knew this was going to happen.\x02\x03",

            "#702FSo, the next trial Ouroboros spoke of...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6287():
        OP_6D(1100, 0, 147600, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6287)

    def lambda_629F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_629F)
    Sleep(50)

    def lambda_62B2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62B2)

    def lambda_62C0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_62C0)
    Sleep(50)

    def lambda_62D3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_62D3)

    def lambda_62E1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_62E1)
    Sleep(50)

    def lambda_62F4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_62F4)

    def lambda_6302():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6302)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #201
        0x102,
        (
            "#1043F#4PYes, it must be this.\x02\x03",

            "#1042FAnd now, they're effectively\x01",
            "holding Grancel hostage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x16,
        (
            "#118F#6PThey can storm in and take the capital\x01",
            "again whenever they please.\x02\x03",

            "It's one way of sending a message, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x102,
        (
            "#1035F#4PThere's another problem.\x02\x03",

            "#1042FI suspect Dad was keeping you\x01",
            "as an ace in the hole.\x02\x03",

            "A special joker card he could play, someone\x01",
            "he could dispatch anywhere an emergency\x01",
            "occurred where he couldn't be.\x02\x03",

            "But now he's played that card,\x01",
            "and you'll have to remain here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x16,
        "#113F#6PBlast it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x15,
        "#703F#6POuroboros certainly plays a hard game...\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xC)
    Sleep(500)
    TurnDirection(0xC, 0x8, 400)

    ChrTalk(    #206
        0xC,
        (
            "#402F#6P...Grandmother.\x02\x03",

            "Allow me to go to Haken Gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6689():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6689)

    def lambda_6697():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6697)
    Sleep(50)

    def lambda_66AA():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_66AA)

    def lambda_66B8():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_66B8)
    Sleep(50)

    def lambda_66CB():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_66CB)

    def lambda_66D9():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_66D9)

    ChrTalk(    #207
        0x101,
        "#1004F#2PSay WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        "#1044F#4PKloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xC,
        (
            "#406F#6PI couldn't bear sending Uncle... He risked\x01",
            "his life once already for our sakes.\x02\x03",

            "#402FLet me go. I will negotiate with the\x01",
            "Erebonians as your agent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x8,
        (
            "#094F#6P...Very well.\x02\x03",

            "#092FThough we may have signed a non-aggression pact\x01",
            "with them, remember that the scales on which\x01",
            "Erebonia and Liberl balance are still unstable.\x02\x03",

            "These events could spiral into chaos\x01",
            "that would engulf the continent.\x02\x03",

            "#090FI am counting on you...to balance \x01",
            "those scales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xC,
        "#401F#6PI will!\x02",
    )

    CloseMessageWindow()

    def lambda_68F7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68F7)
    Sleep(80)

    def lambda_690A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_690A)
    Sleep(80)

    def lambda_691D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_691D)
    Sleep(80)

    def lambda_6930():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6930)
    Sleep(80)

    def lambda_6943():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6943)
    Sleep(80)

    def lambda_6956():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6956)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #212
        "\x07\x05Estelle's group briefly shared a look.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    def lambda_69B0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69B0)
    Sleep(50)

    def lambda_69C3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_69C3)
    Sleep(50)

    def lambda_69D6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_69D6)
    Sleep(50)

    def lambda_69E9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_69E9)
    Sleep(50)

    def lambda_69FC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_69FC)
    Sleep(50)

    def lambda_6A0F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6A0F)
    Sleep(500)

    ChrTalk(    #213
        0x101,
        (
            "#1006F#2PSo, uh...\x02\x03",

            "In that case, mind if we go with you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6ABD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6ABD)
    Sleep(50)

    def lambda_6AD0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6AD0)
    Sleep(50)

    def lambda_6AE3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6AE3)
    Sleep(50)
    OP_8C(0x15, 180, 400)

    ChrTalk(    #214
        0xC,
        "#409F#6PI'm sorry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        (
            "#1040F#4PWe shall see the heiress to\x01",
            "Haken Gate safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xD,
        (
            "#051F#2PAnd if things get really crazy and turn\x01",
            "into a shooting war, we'll do what we\x01",
            "can to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xA,
        (
            "#027FNow mind, we can't actually HELP you with\x01",
            "a shooting war, as per guild protocol...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xF,
        (
            "#071F...But there's a few things we could\x01",
            "do from a neutral position, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xC,
        "#405F#6PEveryone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x8,
        (
            "#090F#6P...I couldn't ask for more.\x02\x03",

            "#091FThank you. Please, keep her safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        "#1006F#2PYes, Your Majesty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x102,
        "#1040F#4PLeave everything to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x16,
        (
            "#115F#6PEstelle, Joshua. On that note.\x02\x03",

            "#110FI and my men will keep an eye on any\x01",
            "movements the society may try to make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x15,
        (
            "#701F#6PEven if they attempt to assault us\x01",
            "with that massive puppet of theirs,\x01",
            "we will be ready to respond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#1025F#2PGuys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        "#1035F#4PWe'll be counting on you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "\x07\x05And so Estelle's group took to the road toward Haken Gate\x01",
            "while escorting Kloe.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #228
        (
            "\x07\x05Passing through Gurune Gate, they moved through Rolent\x01",
            "as quickly as possible...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #229
        "\x07\x05...and soon arrived at Haken Gate.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    ClearChrFlags(0x101, 0x40)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_440D end

    SaveToFile()

Try(main)
