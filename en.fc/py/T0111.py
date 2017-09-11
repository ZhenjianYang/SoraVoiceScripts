from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0111   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0111.x',
        MapIndex            = 11,
        MapDefaultBGM       = "ed60010",
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
        'Fate',                                 # 9
        'Yuni',                                 # 10
        'Radford',                              # 11
        'Euridice',                             # 12
        'Frissa',                               # 13
        'Anya',                                 # 14
        'Freemont',                             # 15
        'Mine Chief Gaton',                     # 16
    )

    DeclEntryPoint(
        Unknown_00              = -76000,
        Unknown_04              = 0,
        Unknown_08              = 32000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -76000,
        Unknown_04              = 0,
        Unknown_08              = 30000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -77000,
        Unknown_04              = 0,
        Unknown_08              = -2000,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 3000,
        Unknown_04              = 0,
        Unknown_08              = 30000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 37000,
        Unknown_04              = 0,
        Unknown_08              = 30000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01170 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01070 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01530 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01170P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01070P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01530P._CP',             # 07
    )

    DeclNpc(
        X                   = 37069,
        Z                   = 0,
        Y                   = 33566,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 38800,
        Z                   = 0,
        Y                   = 30060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -35400,
        Z                   = 0,
        Y                   = 36030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -39940,
        Z                   = 0,
        Y                   = 33130,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4547,
        Z                   = 0,
        Y                   = 37480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 3137,
        Z                   = 0,
        Y                   = 32103,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -35634,
        Z                   = 0,
        Y                   = 31939,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 4600,
        Z                   = 0,
        Y                   = 31530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    ScpFunction(
        "Function_0_2FA",          # 00, 0
        "Function_1_3A1",          # 01, 1
        "Function_2_3C3",          # 02, 2
        "Function_3_3D9",          # 03, 3
        "Function_4_3FD",          # 04, 4
        "Function_5_1802",         # 05, 5
        "Function_6_1A7B",         # 06, 6
        "Function_7_2506",         # 07, 7
        "Function_8_2CF4",         # 08, 8
        "Function_9_2E61",         # 09, 9
        "Function_10_380F",        # 0A, 10
        "Function_11_3C58",        # 0B, 11
    )


    def Function_0_2FA(): pass

    label("Function_0_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_309")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_322")

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_322")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_322")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_32E")
    ClearChrFlags(0xF, 0x80)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_342")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_3A0")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_34C")
    Jump("loc_3A0")

    label("loc_34C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_360")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_3A0")

    label("loc_360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_38C")
    SetChrPos(0xA, -35860, 0, 32500, 172)
    SetChrPos(0xE, -35860, 0, 31320, 357)
    Jump("loc_3A0")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_3A0")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_3A0")

    label("loc_3A0")

    Return()

    # Function_0_2FA end

    def Function_1_3A1(): pass

    label("Function_1_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B9")
    OP_B1("t0111_y")
    Jump("loc_3C2")

    label("loc_3B9")

    OP_B1("t0111_n")

    label("loc_3C2")

    Return()

    # Function_1_3A1 end

    def Function_2_3C3(): pass

    label("Function_2_3C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3C3")

    label("loc_3D8")

    Return()

    # Function_2_3C3 end

    def Function_3_3D9(): pass

    label("Function_3_3D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FC")
    OP_8D(0xFE, -447, 33095, 4354, 30386, 4000)
    Jump("Function_3_3D9")

    label("loc_3FC")

    Return()

    # Function_3_3D9 end

    def Function_4_3FD(): pass

    label("Function_4_3FD")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        (
            "Well, I guess Yuni won't be able\x01",
            "to live under my roof forever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Maybe I should start looking for a husband\x01",
            "for my daughter right now like Rinon's\x01",
            "mother is looking for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Oh, I don't know...but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_534")

    label("loc_4ED")


    ChrTalk(    #3
        0xFE,
        (
            "Well, I guess Yuni won't be able\x01",
            "to live under my roof forever...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_534")

    Jump("loc_17FE")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A8")
    OP_A2(0x2A6)

    ChrTalk(    #4
        0xFE,
        (
            "Rinon's mother came here looking\x01",
            "for a bride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Ha ha, my Yuni is way too young for\x01",
            "the likes of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I can't allow Yuni's husband to be\x01",
            "any less of a man than myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#002F(It's odd to see Fate so heated\x01",
            "up about something.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#010F(It looks like the realization that he's the\x01",
            "father of a young daughter is setting in.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "You seem to be a good match for\x01",
            "my daughter, Joshua...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "But I'm going to have to fail you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#014FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "The reason being: you're too handsome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "It's not that you've done anything\x01",
            "wrong, but I can just see you having\x01",
            "serious girl troubles someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#007FYeah, I can totally see that, too.\x02\x03",

            "#007FJoshua is completely out of touch with\x01",
            "reality. He doesn't even notice that kinda stuff.\x02\x03",

            "And therein lies another problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#018F(I think it's YOU who's out of\x01",
            "touch with reality...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90D")

    label("loc_8A8")


    ChrTalk(    #17
        0xFE,
        (
            "And, Joshua, you're much too old\x01",
            "for Yuni, you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "That's another fail right there!\x02",
    )

    CloseMessageWindow()

    label("loc_90D")

    Jump("loc_17FE")

    label("loc_910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_A37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A04")
    OP_A2(0x0)

    ChrTalk(    #19
        0xFE,
        (
            "Hey there, Estelle, Joshua.\x01",
            "I've heard that the two of you\x01",
            "have been pretty active.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "You're even being referred to as new,\x01",
            "hopeful young bracers around town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I should have expected as much\x01",
            "from Cassius' kids.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A34")

    label("loc_A04")


    ChrTalk(    #22
        0xFE,
        (
            "I'm rooting for you two,\x01",
            "so hang in there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A34")

    Jump("loc_17FE")

    label("loc_A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFB")
    OP_A2(0x0)

    ChrTalk(    #23
        0xFE,
        (
            "10 years ago, the Imperial Army broke\x01",
            "through our borders in great numbers\x01",
            "and trampled the entire kingdom...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "But we were able to drive them out\x01",
            "through a darn near-miraculous,\x01",
            "lightning-quick military operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Without that plan, Rolent would probably\x01",
            "be a part of the Empire's territory today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I was assigned to the unit in Rolent and\x01",
            "fought in the war, but my leg was injured\x01",
            "by a piece of flying shrapnel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C54")

    label("loc_BFB")


    ChrTalk(    #27
        0xFE,
        (
            "Without that plan, Rolent would probably\x01",
            "be a part of the Empire's territory today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C54")

    Jump("loc_17FE")

    label("loc_C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_F0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E93")
    OP_A2(0x2A5)

    ChrTalk(    #28
        0xFE,
        (
            "Have you ever heard anything from\x01",
            "your father about when he was in\x01",
            "the military?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#007FNo...he almost never talks about\x01",
            "anything before he became a bracer.\x02\x03",

            "#000FAlthough, he's often told me about\x01",
            "my mom...\x02\x03",

            "How about you, Joshua?\x01",
            "Have you heard anything from Dad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#010FNo, that goes for me as well.\x02\x03",

            "Even if I ask, he always finds some\x01",
            "way to evade the subject.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#007FYeah, he does that, doesn't he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "At any rate, Liberl is at peace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "And there's nothing I want more than to\x01",
            "have Yuni live in a time of peace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F09")

    label("loc_E93")


    ChrTalk(    #35
        0xFE,
        "At any rate, Liberl is at peace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "And there's nothing I want more than to\x01",
            "have Yuni live in a time of peace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F09")

    Jump("loc_17FE")

    label("loc_F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_119F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111E")
    OP_A2(0x2A4)

    ChrTalk(    #37
        0x8,
        (
            "Of all things, I heard that Pat and\x01",
            "Luke took off to the tower north of\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "I also heard that you rescued them\x01",
            "as they were being attacked by\x01",
            "monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "You did well. That's just what I'd\x01",
            "expect from Cassius' kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#007FYeah...uh, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        "What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#010FTo be honest, Dad was the one who\x01",
            "saved us all in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "Ha ha, you kids are still young.\x01",
            "You'll continue to grow and mature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "Yuni came back, too, and so all\x01",
            "I can say is: I'm just glad that\x01",
            "everyone's safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_119C")

    label("loc_111E")


    ChrTalk(    #45
        0x8,
        (
            "You kids are still young.\x01",
            "You'll continue to grow and mature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "All I can say is: I'm just glad that\x01",
            "everyone's safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_119C")

    Jump("loc_17FE")

    label("loc_119F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BE")
    OP_A2(0x0)

    ChrTalk(    #47
        0x8,
        (
            "Yuni should be back any time now,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "That's odd of her not to be\x01",
            "home by now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "Estelle, Joshua. If you see my Yuni,\x01",
            "could you tell her to come home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "She's never broken curfew before,\x01",
            "but...I'm worried because she's\x01",
            "still just a little girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1412")

    label("loc_12BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B1")
    OP_A2(0x1)

    ChrTalk(    #51
        0x8,
        (
            "That reminds me. It seems like she's\x01",
            "always hanging out with Pat and Luke,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "She really doesn't have to play\x01",
            "around with those boys all the\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#501FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "Oh, it's nothing.\x01",
            "I was just thinking out loud.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1412")

    label("loc_13B1")


    ChrTalk(    #55
        0x8,
        (
            "She's never broken curfew before,\x01",
            "but...I'm worried because she's\x01",
            "still just a little girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1412")

    Jump("loc_17FE")

    label("loc_1415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1787")
    OP_A2(0x2A3)

    ChrTalk(    #56
        0x8,
        (
            "Well, look what the cat dragged in!\x01",
            "Estelle and Joshua, how've ya been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#000FGood morning, Mr. Fate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        "#010FGood morning, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "How's your father, Cassius?\x01",
            "Is he doing well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#000FYep, he's doing so well it might even surprise you.\x02\x03",

            "#000FI don't think there's anyone else his age who's in\x01",
            "such good shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "Ha ha, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "My daughter's really wanted to see him,\x01",
            "but he hasn't shown his face around here in a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "Could you give him a message for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "Tell him that Fate says he'd like to talk about the\x01",
            "old days sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        "#010FSure. We'll tell him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#000F(Hey, Joshua...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #67
        0x101,
        (
            "#000F(How does Mr. Fate know Dad so well, again?)\x02\x03",

            "#000F(I know they're friends and all, but...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #68
        0x102,
        (
            "#010F(I've heard that they were battle buddies during their days\x01",
            "in the Royal Army.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#000F(Oh yeah, that's right.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_17FE")

    label("loc_1787")


    ChrTalk(    #70
        0x8,
        (
            "Please tell your father to stop by again\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "I'd really like to talk with him about the good old\x01",
            "days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FE")

    TalkEnd(0x8)
    Return()

    # Function_4_3FD end

    def Function_5_1802(): pass

    label("Function_5_1802")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_183B")

    ChrTalk(    #72
        0xFE,
        "Papa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "I'm only seven years old.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A77")

    label("loc_183B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_189D")

    ChrTalk(    #74
        0xFE,
        (
            "My papa's been asking me some\x01",
            "weird things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Like who I'd choose, Luke or Pat?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A77")

    label("loc_189D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_192D")

    ChrTalk(    #76
        0x9,
        (
            "Today, I'm gonna stay with my papa\x01",
            "and help him with some things around\x01",
            "the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "My papa's so happy when\x01",
            "I stay with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A77")

    label("loc_192D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1A77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FA")
    OP_A2(0x2)

    ChrTalk(    #78
        0x9,
        "Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        "Thanks for rescuing Luke and Pat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "Miss Holden was talking lots about\x01",
            "you guys and saying that you did\x01",
            "a great job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#501FAhhaha... Thanks, Yuni.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A77")

    label("loc_19FA")


    ChrTalk(    #82
        0x9,
        "Thanks for rescuing Luke and Pat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "Miss Holden was talking lots about\x01",
            "you guys and saying that you did\x01",
            "a great job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A77")

    TalkEnd(0x9)
    Return()

    # Function_5_1802 end

    def Function_6_1A7B(): pass

    label("Function_6_1A7B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B98")
    OP_A2(0x3)

    ChrTalk(    #84
        0xFE,
        (
            "The young kids these days only tend\x01",
            "to focus on profit as a way to gain\x01",
            "acceptance from others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "But, back in my day, if we wanted to\x01",
            "be accepted, we had to work hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "It's like my daughter says.\x01",
            "We'll have to watch these kids\x01",
            "with a careful eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C38")

    label("loc_1B98")


    ChrTalk(    #87
        0xFE,
        (
            "Back in my day, if we wanted to\x01",
            "be accepted as an adult, we had\x01",
            "to work hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Maybe I need to do like my daughter\x01",
            "suggests and keep an eye on things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C38")

    Jump("loc_2502")

    label("loc_1C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D95")
    OP_A2(0x3)

    ChrTalk(    #89
        0xFE,
        (
            "In the timber industry, woodsmen don't\x01",
            "just grow trees to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Woodsmen watch over the forests,\x01",
            "live with the forests, and give thanks\x01",
            "for their bounteous blessings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "When a person can do all of these, then\x01",
            "they can be called a real woodsman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "My daughter's husband is still half\x01",
            "a man in that respect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E52")

    label("loc_1D95")


    ChrTalk(    #93
        0xFE,
        (
            "Woodsmen watch over the forests,\x01",
            "live with the forests, and give thanks\x01",
            "for their bounteous blessings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "When a person can do all of these, then\x01",
            "they can be called a real woodsman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E52")

    Jump("loc_2502")

    label("loc_1E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F82")
    OP_A2(0x3)

    ChrTalk(    #95
        0xFE,
        (
            "If my lower back hadn't given me\x01",
            "all this trouble, I'd still be working\x01",
            "in the forest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "It's too bad that my body aches as\x01",
            "bad as it does at this age. I still\x01",
            "want to get out there and work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I feel a bit insecure about my\x01",
            "daughter's husband working out\x01",
            "there alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202E")

    label("loc_1F82")


    ChrTalk(    #98
        0xFE,
        (
            "If my lower back hadn't given me\x01",
            "all this trouble, I'd still be working\x01",
            "in the forest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "I feel a bit insecure about my\x01",
            "daughter's husband working out\x01",
            "there alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202E")

    Jump("loc_2502")

    label("loc_2031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_21F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2153")
    OP_A2(0x3)

    ChrTalk(    #100
        0xA,
        (
            "Hmph, my son-in-law shouldn't be\x01",
            "getting all cocky just because he's\x01",
            "gotten a little better at the work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "He's still not fit to be my successor\x01",
            "or my daughter's husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "He needs to be able to bear the\x01",
            "weight of Rolent's timber industry\x01",
            "on his shoulders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F2")

    label("loc_2153")


    ChrTalk(    #103
        0xA,
        (
            "He's still not fit to be my successor\x01",
            "or my daughter's husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "He needs to be able to bear the\x01",
            "weight of Rolent's timber industry\x01",
            "on his shoulders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F2")

    Jump("loc_2502")

    label("loc_21F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2311")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B7")
    OP_A2(0x3)

    ChrTalk(    #105
        0xA,
        "Hic!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "Hmph, my son-in-law is still half a\x01",
            "man when it comes to this business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        (
            "This isn't an easy job, and it takes\x01",
            "a good 2-3 years to become a real\x01",
            "woodsman.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230E")

    label("loc_22B7")


    ChrTalk(    #108
        0xA,
        "Hic!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "Hmph, my son-in-law is still half a\x01",
            "man when it comes to this business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230E")

    Jump("loc_2502")

    label("loc_2311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244A")
    OP_A2(0x3)

    ChrTalk(    #110
        0xA,
        (
            "Farming, mining and timber. Those are the\x01",
            "three major industries here in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "It's no exaggeration to say that these\x01",
            "industries are what support Rolent\x01",
            "economically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xA,
        (
            "The timber industry, which grows forests\x01",
            "and in turn uses the trees as a resource,\x01",
            "began at Queen Alicia's behest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2502")

    label("loc_244A")


    ChrTalk(    #113
        0xA,
        (
            "No matter how abundant the woods\x01",
            "and forests are here in Rolent,\x01",
            "they're not limitless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        (
            "Her Majesty the Queen has a good\x01",
            "head on her shoulders and a real\x01",
            "knack for business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2502")

    TalkEnd(0xA)
    Return()

    # Function_6_1A7B end

    def Function_7_2506(): pass

    label("Function_7_2506")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25BB")
    OP_A2(0x4)

    ChrTalk(    #115
        0xFE,
        (
            "Recently, my husband and father have\x01",
            "started opening up to each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I'm so glad... There's nothing better\x01",
            "than having a warm and loving family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2621")

    label("loc_25BB")


    ChrTalk(    #117
        0xFE,
        (
            "I guess it was worth all the trouble\x01",
            "I went through to lecture my father\x01",
            "about family relations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2621")

    Jump("loc_2CF0")

    label("loc_2624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2794")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2706")
    OP_A2(0x4)

    ChrTalk(    #118
        0xFE,
        (
            "My father has stopped complaining\x01",
            "about the work my husband does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "But, it does look like he's holding\x01",
            "his tongue all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I'm sure he'd feel much better if\x01",
            "he just said what he felt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2791")

    label("loc_2706")


    ChrTalk(    #121
        0xFE,
        (
            "My father has stopped complaining\x01",
            "about the work my husband does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "But, it does look like he's holding\x01",
            "his tongue all the time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2791")

    Jump("loc_2CF0")

    label("loc_2794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_27FF")

    ChrTalk(    #123
        0xFE,
        (
            "Recently, my father has been\x01",
            "grumbling about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "I wonder what's on his mind...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CF0")

    label("loc_27FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2890")

    ChrTalk(    #125
        0xFE,
        (
            "Recently, my husband has been\x01",
            "doing well with his work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I wish my father would just recognize\x01",
            "him as a suitable successor...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF0")

    label("loc_2890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2A07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_296C")
    OP_A2(0x4)

    ChrTalk(    #127
        0xFE,
        (
            "I was just thinking about this as\x01",
            "I was out shopping, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "It seems like there are a lot less\x01",
            "quality vegetables now than there\x01",
            "used to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I wonder if it was just my\x01",
            "imagination...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_296C")


    ChrTalk(    #130
        0xFE,
        (
            "I was just thinking about this as\x01",
            "I was out shopping, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "It seems like there are a lot less\x01",
            "quality vegetables now than there\x01",
            "used to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A04")

    Jump("loc_2CF0")

    label("loc_2A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_2B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADA")
    OP_A2(0x4)

    ChrTalk(    #132
        0xB,
        "Here we go again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "My father is overly strict with\x01",
            "my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        (
            "My husband works so hard. I wish my father\x01",
            "would give him some time to adjust to the\x01",
            "work without complaining.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7F")

    label("loc_2ADA")


    ChrTalk(    #135
        0xB,
        (
            "My father is overly strict with\x01",
            "my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        (
            "My husband works so hard. I wish my father\x01",
            "would give him some time to adjust to the\x01",
            "work without complaining.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7F")

    Jump("loc_2CF0")

    label("loc_2B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2BFA")

    ChrTalk(    #137
        0xB,
        (
            "It's almost time for my husband\x01",
            "to come home from work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        (
            "I'd better get to work on preparing\x01",
            "dinner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF0")

    label("loc_2BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9C")
    OP_A2(0x4)

    ChrTalk(    #139
        0xB,
        (
            "Let's see here, it looks like my\x01",
            "husband's gone to work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xB,
        (
            "I'd better do the housework quickly\x01",
            "and head out to take care of the\x01",
            "shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF0")

    label("loc_2C9C")


    ChrTalk(    #141
        0xB,
        (
            "I'd better do the housework quickly\x01",
            "and head out to take care of the\x01",
            "shopping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF0")

    TalkEnd(0xB)
    Return()

    # Function_7_2506 end

    def Function_8_2CF4(): pass

    label("Function_8_2CF4")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_2E5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD9")
    OP_A2(0x7)

    ChrTalk(    #142
        0xE,
        "Man I'm beat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xE,
        (
            "I just managed to get enough wood\x01",
            "out for the order I received.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xE,
        (
            "But my father-in-law won't even\x01",
            "acknowledge my efforts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xE,
        (
            "I guess I'm just going to have to\x01",
            "work harder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_2DD9")


    ChrTalk(    #146
        0xE,
        (
            "I just managed to get enough wood\x01",
            "out for the order I received.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xE,
        (
            "But my father-in-law won't even\x01",
            "acknowledge my efforts...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E5D")

    TalkEnd(0xE)
    Return()

    # Function_8_2CF4 end

    def Function_9_2E61(): pass

    label("Function_9_2E61")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2FFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F76")
    OP_A2(0x6)

    ChrTalk(    #148
        0xFE,
        (
            "My husband finally came home\x01",
            "from the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I wonder how many days it's been\x01",
            "since he was here before now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "My daughter is ecstatic and I've prepared\x01",
            "a wonderful meal to celebrate. It's been a\x01",
            "while since we've eaten together as a family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF8")

    label("loc_2F76")


    ChrTalk(    #151
        0xFE,
        (
            "Today will be the first time in a while\x01",
            "that we've all been together as a family.\x01",
            "I'll need to make something extra special.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF8")

    Jump("loc_380B")

    label("loc_2FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_319D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30FE")
    OP_A2(0x6)

    ChrTalk(    #152
        0xFE,
        (
            "I received word from my husband\x01",
            "today that he'll be finishing up\x01",
            "with his current job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "Heehee...\x01",
            "I think I'd better cook something\x01",
            "extra special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "The longer we are apart, the deeper\x01",
            "the bond grows between my husband\x01",
            "and I.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_319A")

    label("loc_30FE")


    ChrTalk(    #155
        0xFE,
        (
            "I received word from my husband\x01",
            "today that he'll be finishing up\x01",
            "with his current job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "Heehee...\x01",
            "I think I'd better cook something\x01",
            "extra special.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319A")

    Jump("loc_380B")

    label("loc_319D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_320F")

    ChrTalk(    #157
        0xFE,
        (
            "I heard rumors that some fiends\x01",
            "appeared in the mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "I wonder if my husband's all right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_380B")

    label("loc_320F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D8")
    OP_A2(0x6)

    ChrTalk(    #159
        0xFE,
        (
            "I just received word from the mine\x01",
            "where my husband works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "It seems like they discovered something\x01",
            "incredible in a new lode.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "I wonder what it was that they found...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3360")

    label("loc_32D8")


    ChrTalk(    #162
        0xFE,
        (
            "It seems like something incredible\x01",
            "was discovered in the mine where\x01",
            "my husband works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "I wonder what it was that they found...\x02",
    )

    CloseMessageWindow()

    label("loc_3360")

    Jump("loc_380B")

    label("loc_3363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_34C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3473")
    OP_A2(0x6)

    ChrTalk(    #164
        0xFE,
        (
            "My husband who manages the mine\x01",
            "works so hard, so I need to work\x01",
            "hard, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "When I think about things in this way,\x01",
            "strangely I don't feel lonely that we're\x01",
            "apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "Heehee! I guess this is just\x01",
            "another way of showing each other\x01",
            "our love.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C4")

    label("loc_3473")


    ChrTalk(    #167
        0xFE,
        (
            "My husband who manages the mine\x01",
            "works so hard, so I need to work\x01",
            "hard, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C4")

    Jump("loc_380B")

    label("loc_34C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_3578")

    ChrTalk(    #168
        0xC,
        (
            "I just received word from my husband\x01",
            "that they discovered a new lode in\x01",
            "the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xC,
        (
            "Unfortunately, it'll only be my daughter\x01",
            "and I at home for dinner tonight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_380B")

    label("loc_3578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_36FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3663")
    OP_A2(0x6)

    ChrTalk(    #170
        0xC,
        (
            "I've already started dinner for\x01",
            "the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xC,
        (
            "I'm making plenty, so hopefully my\x01",
            "husband will be coming home today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xC,
        (
            "Staying overnight in the mine and\x01",
            "working through the night is pretty\x01",
            "common for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_3663")


    ChrTalk(    #173
        0xC,
        (
            "I wonder if my husband will be\x01",
            "coming home today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xC,
        (
            "Staying overnight in the mine and\x01",
            "working through the night is pretty\x01",
            "common for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F7")

    Jump("loc_380B")

    label("loc_36FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A8")
    OP_A2(0x6)

    ChrTalk(    #175
        0xC,
        (
            "My husband works in the Malga\x01",
            "Mine to the north of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xC,
        "He left here at the crack of dawn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xC,
        (
            "Sometimes he doesn't even come\x01",
            "home for days on end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_380B")

    label("loc_37A8")


    ChrTalk(    #178
        0xC,
        (
            "I hope he doesn't get burned out\x01",
            "from working so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xC,
        "I'm always worrying about that.\x02",
    )

    CloseMessageWindow()

    label("loc_380B")

    TalkEnd(0xC)
    Return()

    # Function_9_2E61 end

    def Function_10_380F(): pass

    label("Function_10_380F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_38C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388C")
    OP_A2(0x5)

    ChrTalk(    #180
        0xFE,
        "My daddy's here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "He just came home and he even\x01",
            "said he would play with me later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "Yay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_38C0")

    label("loc_388C")


    ChrTalk(    #183
        0xFE,
        (
            "I want to play with my daddy as\x01",
            "soon as I can!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38C0")

    Jump("loc_3C54")

    label("loc_38C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_39A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_395B")
    OP_A2(0x5)

    ChrTalk(    #184
        0xFE,
        "I'm so excited!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "Listen! Listen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "My daddy's coming home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "I hope he'll be home soon.\x01",
            "I want us to play together!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399F")

    label("loc_395B")


    ChrTalk(    #188
        0xFE,
        (
            "I hope my daddy will be home soon.\x01",
            "I want us to play together!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399F")

    Jump("loc_3C54")

    label("loc_39A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_39E8")

    ChrTalk(    #189
        0xFE,
        "My mommy's kind of sad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "I wonder what happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C54")

    label("loc_39E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3A99")

    ChrTalk(    #191
        0xFE,
        (
            "When my daddy's not around,\x01",
            "I do my best to help out my mommy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "I help her with the cooking, cleaning,\x01",
            "and laundry, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "Don't you think I'm a big help?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C54")

    label("loc_3A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3AF5")

    ChrTalk(    #194
        0xFE,
        (
            "I'm gonna start going to Sunday\x01",
            "School soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "I wonder if school is fun?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C54")

    label("loc_3AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_3B44")

    ChrTalk(    #196
        0xD,
        (
            "Daddy said he can't come home\x01",
            "from work today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xD,
        "*sniffle*\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C54")

    label("loc_3B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_3B9D")

    ChrTalk(    #198
        0xD,
        "I love my daddy so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xD,
        (
            "He's so strong, and he's always\x01",
            "nice to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C54")

    label("loc_3B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C27")
    OP_A2(0x5)

    ChrTalk(    #200
        0xD,
        "My daddy's job is digging holes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xD,
        "And he finds lots of pretty rocks inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xD,
        "He says they're called sep-ti-um.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C54")

    label("loc_3C27")


    ChrTalk(    #203
        0xD,
        (
            "My daddy says his job is digging\x01",
            "holes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C54")

    TalkEnd(0xD)
    Return()

    # Function_10_380F end

    def Function_11_3C58(): pass

    label("Function_11_3C58")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DAA")
    OP_A2(0x8)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #204
        0xFE,
        (
            "Well, if it isn't the two bracers\x01",
            "from the other day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        (
            "#000FWait, you're the mine chief from\x01",
            "the Malga...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "I want you to know that you really\x01",
            "helped me out the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "The monster scare has finally\x01",
            "settled down, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "So I was finally able to make it\x01",
            "home for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DE7")

    label("loc_3DAA")


    ChrTalk(    #209
        0xFE,
        (
            "Things are much more relaxing\x01",
            "at home, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE7")

    TalkEnd(0xF)
    Return()

    # Function_11_3C58 end

    SaveToFile()

Try(main)
