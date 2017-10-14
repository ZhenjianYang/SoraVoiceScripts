from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4131   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Archbishop Currant',                   # 9
        'Bishop Reval',                         # 10
        'Sister Noah',                          # 11
        'Cisna',                                # 12
        'Agate',                                # 13
        'Scherazard',                           # 14
        'Worshipper',                           # 15
        'Worshipper',                           # 16
        'Worshipper',                           # 17
        'Worshipper',                           # 18
        'Worshipper',                           # 19
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01670 ._CH',             # 01
        'ED6_DT07/CH01410 ._CH',             # 02
        'ED6_DT07/CH01033 ._CH',             # 03
        'ED6_DT07/CH00050 ._CH',             # 04
        'ED6_DT07/CH00020 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
        'ED6_DT07/CH01010 ._CH',             # 07
        'ED6_DT07/CH01143 ._CH',             # 08
        'ED6_DT07/CH01160 ._CH',             # 09
        'ED6_DT07/CH01220 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01670P._CP',             # 01
        'ED6_DT07/CH01410P._CP',             # 02
        'ED6_DT07/CH01033P._CP',             # 03
        'ED6_DT07/CH00050P._CP',             # 04
        'ED6_DT07/CH00020P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
        'ED6_DT07/CH01010P._CP',             # 07
        'ED6_DT07/CH01143P._CP',             # 08
        'ED6_DT07/CH01160P._CP',             # 09
        'ED6_DT07/CH01220P._CP',             # 0A
    )

    DeclNpc(
        X                   = -50,
        Z                   = 1000,
        Y                   = 20410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2870,
        Z                   = 1000,
        Y                   = 18870,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -71360,
        Z                   = 0,
        Y                   = 3640,
        Direction           = 82,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -3190,
        Z                   = 150,
        Y                   = 10800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 910,
        Z                   = 0,
        Y                   = 14450,
        Direction           = 260,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 910,
        Z                   = 0,
        Y                   = 14450,
        Direction           = 260,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3890,
        Z                   = 1000,
        Y                   = 17280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -2690,
        Z                   = 1000,
        Y                   = 17280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 3990,
        Z                   = 150,
        Y                   = 4660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4970,
        Z                   = 0,
        Y                   = 5260,
        Direction           = 210,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -5300,
        Z                   = 0,
        Y                   = 7270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = 200,
        TriggerZ            = 1000,
        TriggerY            = 17890,
        TriggerRange        = 400,
        ActorX              = -50,
        ActorZ              = 2500,
        ActorY              = 20410,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74990,
        TriggerZ            = 0,
        TriggerY            = 66030,
        TriggerRange        = 800,
        ActorX              = -74990,
        ActorZ              = 1000,
        ActorY              = 66030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_3C0",          # 01, 1
        "Function_2_3E6",          # 02, 2
        "Function_3_3EB",          # 03, 3
        "Function_4_CDE",          # 04, 4
        "Function_5_13A9",         # 05, 5
        "Function_6_19B9",         # 06, 6
        "Function_7_1C3B",         # 07, 7
        "Function_8_1CE8",         # 08, 8
        "Function_9_1D75",         # 09, 9
        "Function_10_1EB0",        # 0A, 10
        "Function_11_2021",        # 0B, 11
        "Function_12_21A2",        # 0C, 12
        "Function_13_22ED",        # 0D, 13
        "Function_14_2497",        # 0E, 14
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2DE")
    SetChrPos(0xA, -132010, 0, 6440, 340)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_3BF")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_31B")
    SetChrPos(0xA, -132010, 0, 6440, 340)
    SetChrPos(0xE, 3250, 0, 13250, 344)
    SetChrPos(0xF, 4130, 0, 13250, 347)
    Jump("loc_3BF")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_369")
    SetChrPos(0x9, -132010, 0, 6440, 340)
    SetChrPos(0xA, -75250, 0, 3670, 275)
    SetChrPos(0xE, 3250, 0, 13250, 344)
    SetChrPos(0xF, 4130, 0, 13250, 347)
    Jump("loc_3BF")

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x9, -132010, 0, 6440, 340)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2")
    SetChrPos(0xA, -540, 0, 14500, 103)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3AD")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3B2")

    label("loc_3AD")

    ClearChrFlags(0xD, 0x80)

    label("loc_3B2")

    Jump("loc_3BF")

    label("loc_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3BF")
    Jump("loc_3BF")

    label("loc_3BF")

    Return()

    # Function_0_2AA end

    def Function_1_3C0(): pass

    label("Function_1_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DC")
    OP_B1("t4131_y")
    Jump("loc_3E5")

    label("loc_3DC")

    OP_B1("t4131_n")

    label("loc_3E5")

    Return()

    # Function_1_3C0 end

    def Function_2_3E6(): pass

    label("Function_2_3E6")

    Call(0, 3)
    Return()

    # Function_2_3E6 end

    def Function_3_3EB(): pass

    label("Function_3_3EB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_45C")

    ChrTalk(    #0
        0x8,
        "So it's begun, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "This occurrence is no trial from\x01",
            "the Goddess, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDA")

    label("loc_45C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_6BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD")

    ChrTalk(    #3
        0x8,
        (
            "From the perspective of stopping the\x01",
            "Special Ops soldiers, he was correct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "However, his mission should be to recover\x01",
            "artifacts. That is the priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "Spilled milk cannot be re-bottled...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Though nothing can be done, that does\x01",
            "not mean he will not be punished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Of course, he... Father Kevin was\x01",
            "well aware of that, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6BA")

    label("loc_5CD")


    ChrTalk(    #8
        0x8,
        (
            "From the perspective of stopping the\x01",
            "Special Ops soldiers, he was correct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "However, his mission should be to recover\x01",
            "artifacts. That is the priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "Though nothing can be done, that does\x01",
            "not mean he will not be punished.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BA")

    Jump("loc_CDA")

    label("loc_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_78C")

    ChrTalk(    #11
        0x8,
        (
            "...A girl in a white dress?\x01",
            "No, she hasn't come here, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "A few days ago, there was a girl matching\x01",
            "that description who came here with her\x01",
            "parents, but I haven't seen her since.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDA")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96B")

    ChrTalk(    #13
        0x8,
        (
            "A short while ago, we had an inquiry from\x01",
            "the History Museum about an artifact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "It is true that the church has a duty\x01",
            "to collect and investigate artifacts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "It is also true that there are special\x01",
            "organizations within the church\x01",
            "dedicated to that purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "Why, you ask? Because the church\x01",
            "itself is a neutral body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "The artifact delivered to the History Museum\x01",
            "had lost its power, however, and isn't part\x01",
            "of our collection mission.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_A63")

    label("loc_96B")


    ChrTalk(    #18
        0x8,
        (
            "It is true that the church has a duty\x01",
            "to collect and investigate artifacts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "It is also true that there are special\x01",
            "organizations within the church\x01",
            "dedicated to that purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "Why, you ask? Because the church\x01",
            "itself is a neutral body.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A63")

    Jump("loc_CDA")

    label("loc_A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_B8C")

    ChrTalk(    #21
        0x8,
        (
            "This cathedral has been affiliated with\x01",
            "the Liberl royal family for many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "We accepted our role in the signing\x01",
            "ceremony as part of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "However, the church is ultimately neutral...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "All we can really do is pray to the Goddess,\x01",
            "and watch over the proceedings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDA")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_CDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8A")
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #25
        0x8,
        "Oh, are you the one he spoke of, perhaps?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1015FWho's 'he'?\x02\x03",

            "#1016FI don't think I know anyone here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "The Goddess saves those who\x01",
            "save themselves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "May you find good guidance.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_CDA")

    label("loc_C8A")


    ChrTalk(    #29
        0x8,
        (
            "The Goddess saves those who save themselves...\x01",
            "May you find good guidance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDA")

    TalkEnd(0x8)
    Return()

    # Function_3_3EB end

    def Function_4_CDE(): pass

    label("Function_4_CDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E03")

    ChrTalk(    #30
        0xFE,
        (
            "A little while ago, I got a package for Father\x01",
            "Kevin from a suspicious-looking pair of men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "It isn't that big, but it's wrapped very tightly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I was told by the archbishop to deliver\x01",
            "it as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "But I can't help wondering what's in it...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_E9B")

    label("loc_E03")


    ChrTalk(    #34
        0xFE,
        (
            "A little while ago, I got a package for Father\x01",
            "Kevin from a suspicious-looking pair of men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "It isn't that big, but it's wrapped very tightly.\x02",
    )

    CloseMessageWindow()

    label("loc_E9B")

    Jump("loc_13A5")

    label("loc_E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F83")

    ChrTalk(    #36
        0xFE,
        (
            "I don't know much about Gralsritter,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Not even the archbishop has a full grasp\x01",
            "on them, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Given the nature of Gralsritter's duties,\x01",
            "I suppose that's to be expected, but still...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_FE7")

    label("loc_F83")


    ChrTalk(    #39
        0xFE,
        (
            "I don't know much about Gralsritter,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "I don't know much about Gralsritter,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE7")

    Jump("loc_13A5")

    label("loc_FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_108A")

    ChrTalk(    #41
        0xFE,
        (
            "Oh, you seem to be bearing some troubles,\x01",
            "my child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Oh, Goddess of the Sky, reveal the path beneath\x01",
            "the feet of those who lose their way...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A5")

    label("loc_108A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1122")

    ChrTalk(    #43
        0xFE,
        "We just finished evening mass a short while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I believe I saw a bracer here during that time,\x01",
            "in fact. Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A5")

    label("loc_1122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_11FD")

    ChrTalk(    #45
        0xFE,
        (
            "Father Kevin, dispatched from the\x01",
            "High Seat, is quite the odd one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "He's rather frivolous for a holy man,\x01",
            "giving me ample cause for concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Perhaps many of the traveling\x01",
            "priests are like him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A5")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_13A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1312")

    ChrTalk(    #48
        0xFE,
        (
            "The other day, when I visited the Sanktheim\x01",
            "Gate, I felt the earthquakes that everyone's\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Though they are over now, the folks in\x01",
            "Zeiss must still be quite nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "After all, earthquakes can happen suddenly,\x01",
            "with no warning...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_13A5")

    label("loc_1312")


    ChrTalk(    #51
        0xFE,
        (
            "Though they are over now, the folks in\x01",
            "Zeiss must still be quite nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "After all, earthquakes can happen suddenly,\x01",
            "with no warning...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A5")

    TalkEnd(0xFE)
    Return()

    # Function_4_CDE end

    def Function_5_13A9(): pass

    label("Function_5_13A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1495")

    ChrTalk(    #53
        0xFE,
        (
            "Father Kevin was up late talking\x01",
            "to the archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "After that, he left right away...\x01",
            "And he still hasn't come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "There was some kind of understanding\x01",
            "about this between the archbishop\x01",
            "and Father Kevin...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B5")

    label("loc_1495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_155B")

    ChrTalk(    #56
        0xFE,
        (
            "There were a number of injured people\x01",
            "amongst the Royal Guard following last\x01",
            "night's incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Ohh, Goddess of the Sky, Aidios...\x01",
            "Bestow your blessings on the brave and proud...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B5")

    label("loc_155B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1614")

    ChrTalk(    #58
        0xFE,
        (
            "We received a package addressed to\x01",
            "Father Kevin, which I'd like to deliver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "But he hasn't returned to the cathedral.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "Really, where on earth could he have gone?\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B5")

    label("loc_1614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_16C0")

    ChrTalk(    #61
        0xFE,
        (
            "A bracer just came to inquire about\x01",
            "the threat letter we received.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I would imagine the bracer in question\x01",
            "is back at the guild now, however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1710")

    label("loc_16C0")


    ChrTalk(    #63
        0xFE,
        (
            "Those parents and their child were quite\x01",
            "striking. I remember them well...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1710")

    Jump("loc_19B5")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_18F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183F")

    ChrTalk(    #64
        0xFE,
        (
            "Not long ago, I met the traveling\x01",
            "priest, Father Kevin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I've heard from the archbishop that the work\x01",
            "of a traveling priest is quite difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "But judging by Father Kevin's demeanor,\x01",
            "I don't get that impression at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "Perhaps it's easier than I thought...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_18EE")

    label("loc_183F")


    ChrTalk(    #68
        0xFE,
        (
            "I've heard from the archbishop that the work\x01",
            "of a traveling priest is quite difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "But judging by Father Kevin's demeanor,\x01",
            "I don't get that impression at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EE")

    Jump("loc_19B5")

    label("loc_18F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_19B5")

    ChrTalk(    #70
        0xFE,
        (
            "Phew! All done. I've finally finished\x01",
            "repairing the hymn book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Things have gotten busy ever since\x01",
            "Sister Ellen disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I wonder if we they'll send a\x01",
            "replacement soon...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B5")

    TalkEnd(0xFE)
    Return()

    # Function_5_13A9 end

    def Function_6_19B9(): pass

    label("Function_6_19B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A0A")

    ChrTalk(    #73
        0xFE,
        (
            "This is exactly when we need to\x01",
            "offer our prayers to Aidios...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C37")

    label("loc_1A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1A59")

    ChrTalk(    #74
        0xFE,
        (
            "Oh, Goddess of the Sky, Aidios...\x01",
            "Grant our city peace again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C37")

    label("loc_1A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1A91")

    ChrTalk(    #75
        0xFE,
        "Prayer is the best way to calm the mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C37")

    label("loc_1A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B24")

    ChrTalk(    #76
        0xFE,
        (
            "A short time ago, the head of the\x01",
            "History Museum came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "He was showing the archbishop\x01",
            "something. I wonder what it was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C37")

    label("loc_1B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1BD3")

    ChrTalk(    #78
        0xFE,
        (
            "I hope that the non-aggression pact means we\x01",
            "can be friends with the peoples of the\x01",
            "Republic and the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "Goddess of the Sky...give us your guidance...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C37")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1C37")

    ChrTalk(    #80
        0xFE,
        "Oh, have you come to pray too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "The Goddess of the Sky watches over us all,\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C37")

    TalkEnd(0xFE)
    Return()

    # Function_6_19B9 end

    def Function_7_1C3B(): pass

    label("Function_7_1C3B")

    TalkBegin(0xFE)

    ChrTalk(    #82
        0xC,
        (
            "#050FEstelle, you already finished\x01",
            "with your questionin'?\x02\x03",

            "Mine's still probably gonna take a while,\x01",
            "so if you're done, you can head back to\x01",
            "the guild and wait.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1C3B end

    def Function_8_1CE8(): pass

    label("Function_8_1CE8")

    TalkBegin(0xFE)

    ChrTalk(    #83
        0xD,
        (
            "#020FEstelle, finished with your questioning?\x02\x03",

            "Mine will still take some time, so if you're\x01",
            "done, go back to the guild and wait.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1CE8 end

    def Function_9_1D75(): pass

    label("Function_9_1D75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D82")
    Jump("loc_1EAC")

    label("loc_1D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1DB9")

    ChrTalk(    #84
        0xFE,
        "Prayer is the best way to calm oneself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EAC")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1DE6")

    ChrTalk(    #85
        0xFE,
        "What're ya wishin' for, love?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EAC")

    label("loc_1DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E46")

    ChrTalk(    #86
        0xFE,
        (
            "This stained glass is even prettier with\x01",
            "th' evenin' sun's light through it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAC")

    label("loc_1E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1E7D")

    ChrTalk(    #87
        0xFE,
        "Ha ha, what an incredible glass window.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EAC")

    label("loc_1E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1EAC")

    ChrTalk(    #88
        0xFE,
        "Grancel Cathedral is so big, love.\x02",
    )

    CloseMessageWindow()

    label("loc_1EAC")

    TalkEnd(0xFE)
    Return()

    # Function_9_1D75 end

    def Function_10_1EB0(): pass

    label("Function_10_1EB0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1EBD")
    Jump("loc_201D")

    label("loc_1EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1EFA")

    ChrTalk(    #89
        0xFE,
        (
            "Yes, honey...\x01",
            "This, too, is Aidios' blessing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_201D")

    label("loc_1EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1F6E")

    ChrTalk(    #90
        0xFE,
        "That's my little secret.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "I've heard that telling others\x01",
            "your wishes means they won't\x01",
            "come true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_201D")

    label("loc_1F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA1")

    ChrTalk(    #92
        0xFE,
        "Yes, it's quite breathtaking...\x02",
    )

    CloseMessageWindow()
    Jump("loc_201D")

    label("loc_1FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1FD0")

    ChrTalk(    #93
        0xFE,
        "They call them 'stained glass.'\x02",
    )

    CloseMessageWindow()
    Jump("loc_201D")

    label("loc_1FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_201D")

    ChrTalk(    #94
        0xFE,
        "Yes, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "Our house could easily fit inside of it!\x02",
    )

    CloseMessageWindow()

    label("loc_201D")

    TalkEnd(0xFE)
    Return()

    # Function_10_1EB0 end

    def Function_11_2021(): pass

    label("Function_11_2021")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_202E")
    Jump("loc_219E")

    label("loc_202E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_207F")

    ChrTalk(    #96
        0xFE,
        (
            "Goddess... Please protect my siblings\x01",
            "as they walk the road home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_207F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_20C0")

    ChrTalk(    #97
        0xFE,
        (
            "...Ah, I know. Just a little bit more time,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_20C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2108")

    ChrTalk(    #98
        0xFE,
        (
            "Goddess...\x01",
            "Please forgive my little brother's words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_2108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2159")

    ChrTalk(    #99
        0xFE,
        "Now, close your eyes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "And fold your hands over your heart.\x02",
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_2159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_219E")

    ChrTalk(    #101
        0xFE,
        (
            "Oh, come on...\x01",
            "Can't you stop squirming for ONE SECOND?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219E")

    TalkEnd(0xFE)
    Return()

    # Function_11_2021 end

    def Function_12_21A2(): pass

    label("Function_12_21A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_21AF")
    Jump("loc_22E9")

    label("loc_21AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_21DB")

    ChrTalk(    #102
        0xFE,
        "Hey, come on, let's go home.\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_21DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2240")

    ChrTalk(    #103
        0xFE,
        "You promised to play with me today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "You shouldn't lie in front of the Goddess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_2240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228A")

    ChrTalk(    #105
        0xFE,
        (
            "It's already evenin'...\x01",
            "Mass, pfft. More like torture!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_228A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_22C0")

    ChrTalk(    #106
        0xFE,
        "No, no! I don't wanna pray, neeeeever!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_22C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_22E9")

    ChrTalk(    #107
        0xFE,
        "Churches are so booooring...\x02",
    )

    CloseMessageWindow()

    label("loc_22E9")

    TalkEnd(0xFE)
    Return()

    # Function_12_21A2 end

    def Function_13_22ED(): pass

    label("Function_13_22ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_22FA")
    Jump("loc_2493")

    label("loc_22FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2327")

    ChrTalk(    #108
        0xFE,
        "Goddess, please protect us...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2493")

    label("loc_2327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2367")

    ChrTalk(    #109
        0xFE,
        (
            "Goddess, grant me health and strength\x01",
            "of mind...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2493")

    label("loc_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2397")

    ChrTalk(    #110
        0xFE,
        "Evening mass has just ended.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2493")

    label("loc_2397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_243F")

    ChrTalk(    #111
        0xFE,
        (
            "The solemnity of the cathedral\x01",
            "truly hits one in the heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Perhaps I should come to the cathedral\x01",
            "more often, as the priests and sisters\x01",
            "advise...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2493")

    label("loc_243F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2493")

    ChrTalk(    #113
        0xFE,
        (
            "This is Grancel Cathedral. It's just\x01",
            "as incredible as the rumors say...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2493")

    TalkEnd(0xFE)
    Return()

    # Function_13_22ED end

    def Function_14_2497(): pass

    label("Function_14_2497")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #114
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_2497 end

    SaveToFile()

Try(main)
