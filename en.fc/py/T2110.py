from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2110   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Lytton',                               # 9
        'Ciel',                                 # 10
        'Eletta',                               # 11
        'Gerome',                               # 12
        'Renzo',                                # 13
        'Liz',                                  # 14
        'Antonio',                              # 15
        'Portos',                               # 16
        'Noria',                                # 17
        'Logic',                                # 18
        'Norman',                               # 19
        'Bridget',                              # 20
        'Louis',                                # 21
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH01540 ._CH',             # 01
        'ED6_DT07/CH01170 ._CH',             # 02
        'ED6_DT07/CH01080 ._CH',             # 03
        'ED6_DT07/CH01460 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01690 ._CH',             # 08
        'ED6_DT07/CH01083 ._CH',             # 09
        'ED6_DT07/CH01200 ._CH',             # 0A
        'ED6_DT07/CH01230 ._CH',             # 0B
        'ED6_DT07/CH01470 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH01540P._CP',             # 01
        'ED6_DT07/CH01170P._CP',             # 02
        'ED6_DT07/CH01080P._CP',             # 03
        'ED6_DT07/CH01460P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01690P._CP',             # 08
        'ED6_DT07/CH01083P._CP',             # 09
        'ED6_DT07/CH01200P._CP',             # 0A
        'ED6_DT07/CH01230P._CP',             # 0B
        'ED6_DT07/CH01470P._CP',             # 0C
    )

    DeclNpc(
        X                   = 2009,
        Z                   = 0,
        Y                   = -1890,
        Direction           = 180,
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
        X                   = -5910,
        Z                   = 0,
        Y                   = 5190,
        Direction           = 0,
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
        X                   = -4500,
        Z                   = 4000,
        Y                   = 5750,
        Direction           = 270,
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
        X                   = 1670,
        Z                   = 0,
        Y                   = 1890,
        Direction           = 90,
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
        X                   = 22050,
        Z                   = 0,
        Y                   = -200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 27240,
        Z                   = 0,
        Y                   = -1510,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 26000,
        Z                   = 4000,
        Y                   = -500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 25980,
        Z                   = 0,
        Y                   = 34030,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -2270,
        Z                   = 0,
        Y                   = 37540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2960,
        Z                   = 0,
        Y                   = 33440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -31900,
        Z                   = 0,
        Y                   = 63600,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 24980,
        Z                   = 0,
        Y                   = 62760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 4990,
        Z                   = 0,
        Y                   = 64730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_328",          # 01, 1
        "Function_2_353",          # 02, 2
        "Function_3_369",          # 03, 3
        "Function_4_38D",          # 04, 4
        "Function_5_8FF",          # 05, 5
        "Function_6_FBA",          # 06, 6
        "Function_7_14B5",         # 07, 7
        "Function_8_15FD",         # 08, 8
        "Function_9_1E6B",         # 09, 9
        "Function_10_26A3",        # 0A, 10
        "Function_11_2DB6",        # 0B, 11
        "Function_12_2EAD",        # 0C, 12
        "Function_13_35D8",        # 0D, 13
        "Function_14_3677",        # 0E, 14
        "Function_15_3E53",        # 0F, 15
        "Function_16_41CF",        # 10, 16
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2C6")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    Jump("loc_327")

    label("loc_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2EE")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_327")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_302")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_327")

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_327")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_327")

    Return()

    # Function_0_2B2 end

    def Function_1_328(): pass

    label("Function_1_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_349")
    OP_B1("t2110_y")
    Jump("loc_352")

    label("loc_349")

    OP_B1("t2110_n")

    label("loc_352")

    Return()

    # Function_1_328 end

    def Function_2_353(): pass

    label("Function_2_353")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_368")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_353")

    label("loc_368")

    Return()

    # Function_2_353 end

    def Function_3_369(): pass

    label("Function_3_369")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38C")
    OP_8D(0xFE, 22020, 37800, 27710, 33160, 1500)
    Jump("Function_3_369")

    label("loc_38C")

    Return()

    # Function_3_369 end

    def Function_4_38D(): pass

    label("Function_4_38D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_45E")

    ChrTalk(    #0
        0xFE,
        (
            "Given that the mayor was the face of\x01",
            "Ruan's tourism industry, his arrest\x01",
            "will really ruin the town's image.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "We're already seeing a drop\x01",
            "in the number of visitors and\x01",
            "hotel reservations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FB")

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_5B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        "I used to be a fisherman.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "At least, until the mayor pushed\x01",
            "for the town's focus to change\x01",
            "from fishing to tourism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "My wife suggested that I become\x01",
            "a tour guide instead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B4")

    label("loc_52B")


    ChrTalk(    #5
        0xFE,
        (
            "The mayor pushed for the town's focus\x01",
            "to change from fishing to tourism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "My wife suggested that I become\x01",
            "a tour guide instead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B4")

    Jump("loc_8FB")

    label("loc_5B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_64F")

    ChrTalk(    #7
        0xFE,
        (
            "Just got back from that festival\x01",
            "at my son's school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "It was an excellent break from\x01",
            "work, and my daughter had a great\x01",
            "time as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FB")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_78C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70D")
    OP_A2(0x0)

    ChrTalk(    #9
        0xFE,
        (
            "Let's see...what job to\x01",
            "pursue next...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I'm happiest when my job\x01",
            "keeps me busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "My daughter works as a house-sitter,\x01",
            "but I worry about how lonely she is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_789")

    label("loc_70D")


    ChrTalk(    #12
        0xFE,
        (
            "I'm happiest when my job\x01",
            "keeps me busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "My daughter works as a house-sitter,\x01",
            "but I worry about how lonely she is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_789")

    Jump("loc_8FB")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_8FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_886")
    OP_A2(0x0)

    ChrTalk(    #14
        0xFE,
        (
            "Wow, we've got quite a few\x01",
            "tourists here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "We see a lot of folks coming in\x01",
            "from a long ways off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Being a guide is much more stressful\x01",
            "than being a fisherman...too much\x01",
            "worrying about what everyone else needs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FB")

    label("loc_886")


    ChrTalk(    #17
        0xFE,
        (
            "Being a guide is much more stressful\x01",
            "than being a fisherman...too much\x01",
            "worrying about what everyone else needs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB")

    TalkEnd(0x8)
    Return()

    # Function_4_38D end

    def Function_5_8FF(): pass

    label("Function_5_8FF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_998")

    ChrTalk(    #18
        0xFE,
        (
            "If we really have to elect a new mayor,\x01",
            "I'd prefer it be Mr. Norman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I think he'd do a lot to help build\x01",
            "up the tourism industry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A91")
    OP_A2(0x1)

    ChrTalk(    #20
        0xFE,
        (
            "I'm talking about Mr. Norman,\x01",
            "the owner of the Hotel Blanche.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "He bought an old inn and turned it\x01",
            "into the hotel you see now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "He apparently got along well with\x01",
            "the mayor, since he helped us\x01",
            "get our jobs as guides.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B31")

    label("loc_A91")


    ChrTalk(    #23
        0xFE,
        (
            "I'm talking about Mr. Norman,\x01",
            "the owner of the Hotel Blanche.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "He apparently got along well with\x01",
            "the mayor, since he helped us\x01",
            "get our jobs as guides.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B31")

    Jump("loc_FB6")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57")
    OP_A2(0x1)

    ChrTalk(    #25
        0xFE,
        (
            "That play was really amazing...\x01",
            "And what's more amazing is how\x01",
            "they got that boy into a dress!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "But...I do kinda wish my son could\x01",
            "have been in it... I'm sure he would\x01",
            "have made a great princess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Oh, well. It'd be hard to find\x01",
            "a corset his size, anyway...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA4")

    label("loc_C57")


    ChrTalk(    #28
        0xFE,
        (
            "I went to my son's campus festival.\x01",
            "That play was really a masterpiece.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA4")

    Jump("loc_FB6")

    label("loc_CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBD")
    OP_A2(0x1)

    ChrTalk(    #29
        0xFE,
        (
            "I'm taking some time off work to\x01",
            "attend the festival at my son's\x01",
            "school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I often forget just how much I work.\x01",
            "Poor Eletta always gets stuck looking\x01",
            "after the house, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "When you really think about what's\x01",
            "important, family always wins out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_DBD")


    ChrTalk(    #32
        0xFE,
        (
            "I work specifically to support\x01",
            "my family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I think I lost sight of what\x01",
            "really matters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E20")

    Jump("loc_FB6")

    label("loc_E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F17")
    OP_A2(0x1)

    ChrTalk(    #34
        0xFE,
        (
            "My husband and I both work\x01",
            "as tour guides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "My husband used to be a fisherman,\x01",
            "but you can make more money as\x01",
            "a guide these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "My oldest son goes to the Jenis\x01",
            "Royal Academy, so the expenses\x01",
            "add up quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_F17")


    ChrTalk(    #37
        0xFE,
        (
            "I think my husband wishes he\x01",
            "could've remained a fisherman,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "My oldest son goes to the Jenis\x01",
            "Royal Academy, so the expenses\x01",
            "add up quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB6")

    TalkEnd(0x9)
    Return()

    # Function_5_8FF end

    def Function_6_FBA(): pass

    label("Function_6_FBA")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_101B")

    ChrTalk(    #39
        0xFE,
        (
            "I think my mom and dad are\x01",
            "both home today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "I hope I'll get to go play...\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B1")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1085")

    ChrTalk(    #41
        0xFE,
        (
            "My mom and dad both have today\x01",
            "off from work. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I'm gonna play for as long\x01",
            "as I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B1")

    label("loc_1085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_11A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1134")
    OP_A2(0x2)

    ChrTalk(    #43
        0xFE,
        (
            "I went to my brother's school and\x01",
            "saw lots of stalls and the play\x01",
            "was fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I went to see my brother,\x01",
            "but he got all embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "How come?\x02",
    )

    CloseMessageWindow()
    Jump("loc_119D")

    label("loc_1134")


    ChrTalk(    #46
        0xFE,
        (
            "I went on a trip to my\x01",
            "brother's school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I went to see my brother,\x01",
            "but he got all embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_119D")

    Jump("loc_14B1")

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1235")

    ChrTalk(    #48
        0xFE,
        "Hee hee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "We're all goin' to my brother's\x01",
            "school for the festival soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "My mom's gonna come, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "It's so awesome. ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B1")

    label("loc_1235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1298")

    ChrTalk(    #52
        0xFE,
        (
            "Ummm...I finished the laundry\x01",
            "and sweeping up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "I hope everyone gets back soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B1")

    label("loc_1298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_136F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1348")
    OP_A2(0x2)

    ChrTalk(    #54
        0xFE,
        (
            "I'm looking after the house today,\x01",
            "all by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "My mom and dad are working and\x01",
            "my brother's off at school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "*sniffle*... I'm kinda lonely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_136C")

    label("loc_1348")


    ChrTalk(    #57
        0xFE,
        "*sniffle*... I'm kinda lonely.\x02",
    )

    CloseMessageWindow()

    label("loc_136C")

    Jump("loc_14B1")

    label("loc_136F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_141D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E7")
    OP_A2(0x2)

    ChrTalk(    #58
        0xFE,
        (
            "I gotta go back to house-sitting\x01",
            "tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I hope I can make friends at\x01",
            "Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_13E7")


    ChrTalk(    #60
        0xFE,
        (
            "I hope I can make friends at\x01",
            "Sunday School...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141A")

    Jump("loc_14B1")

    label("loc_141D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_14B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1485")
    OP_A2(0x2)

    ChrTalk(    #61
        0xFE,
        (
            "Okay, I'm done with washing\x01",
            "the clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "My big brother helped me today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B1")

    label("loc_1485")


    ChrTalk(    #63
        0xFE,
        (
            "My mom and dad are both\x01",
            "working today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B1")

    TalkEnd(0xA)
    Return()

    # Function_6_FBA end

    def Function_7_14B5(): pass

    label("Function_7_14B5")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_152C")

    ChrTalk(    #64
        0xFE,
        (
            "Let's see...I'm done with prep\x01",
            "for classes tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Now, what can I do to kill\x01",
            "some time...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F9")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_15F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CD")
    OP_A2(0x3)

    ChrTalk(    #66
        0xFE,
        "I guess I should get ready for school.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I've done everything I need\x01",
            "to get done, so I can't really\x01",
            "complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "That's my motto.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F9")

    label("loc_15CD")


    ChrTalk(    #69
        0xFE,
        "I guess I should get ready for school.\x02",
    )

    CloseMessageWindow()

    label("loc_15F9")

    TalkEnd(0xB)
    Return()

    # Function_7_14B5 end

    def Function_8_15FD(): pass

    label("Function_8_15FD")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_169E")

    ChrTalk(    #70
        0xFE,
        (
            "It's just amazing to me that Mayor\x01",
            "Dalmore was responsible for all\x01",
            "this trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "I'd always thought he was a\x01",
            "good man...boy, was I wrong.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E67")

    label("loc_169E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1720")

    ChrTalk(    #72
        0xFE,
        (
            "Doesn't it cost a lot of mira to\x01",
            "attend school at the Royal\x01",
            "Academy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I don't know what my wife\x01",
            "is thinking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E67")

    label("loc_1720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_187A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E9")
    OP_A2(0x4)

    ChrTalk(    #74
        0xFE,
        (
            "She strong-armed me into going\x01",
            "to visit the place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "...but I have to admit, it seemed\x01",
            "like a nice place to attend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "I wouldn't mind eventually sending\x01",
            "my kid there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1877")

    label("loc_17E9")


    ChrTalk(    #77
        0xFE,
        (
            "If you're going to pursue a\x01",
            "higher education, the Royal\x01",
            "Academy isn't a bad place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "I wouldn't mind eventually sending\x01",
            "my kid there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1877")

    Jump("loc_1E67")

    label("loc_187A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_190A")

    ChrTalk(    #79
        0xFE,
        (
            "They make a really big deal\x01",
            "of this campus festival thing,\x01",
            "don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I wonder why a school would hold\x01",
            "an event like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E67")

    label("loc_190A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A06")
    OP_A2(0x4)

    ChrTalk(    #81
        0xFE,
        (
            "I guess I ought to check out\x01",
            "the campus for myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "But shouldn't we see what the\x01",
            "kid wants, first?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1992():
        TurnDirection(0xD, 0xC, 1000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1992)

    ChrTalk(    #83
        0xD,
        "What was that?\x02",
    )

    CloseMessageWindow()

    def lambda_19B4():
        TurnDirection(0xC, 0xD, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19B4)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #84
        0xFE,
        "...Nothing.\x02",
    )

    CloseMessageWindow()

    def lambda_19EA():
        OP_8C(0xD, 0, 1000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19EA)
    Sleep(700)

    ChrTalk(    #85
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A72")

    label("loc_1A06")


    ChrTalk(    #86
        0xFE,
        (
            "I guess I ought to check out\x01",
            "the campus for myself...\x02\x03",

            "But shouldn't we see what the\x01",
            "kid wants, first?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A72")

    Jump("loc_1E67")

    label("loc_1A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB3")
    OP_A2(0x4)

    ChrTalk(    #87
        0xFE,
        (
            "I've been thinking over this\x01",
            "whole matter with my son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Not so much about whether\x01",
            "I'd prefer he pursue a life\x01",
            "at sea or college...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I think I'd be okay with whatever\x01",
            "he wants, so long as he can make\x01",
            "a decent living.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I hate to admit it, but I'd rather\x01",
            "leave the choice up to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_1BB3")


    ChrTalk(    #91
        0xFE,
        (
            "I think I'd be okay with whatever\x01",
            "my son wants, so long as he can\x01",
            "make a decent living.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "I hate to admit it, but I'd rather\x01",
            "leave the choice up to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C54")

    Jump("loc_1E67")

    label("loc_1C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1CFA")

    ChrTalk(    #93
        0xFE,
        (
            "I'm proud of my life as a sailor,\x01",
            "and that's enough for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I was never any good at school,\x01",
            "but you don't need book\x01",
            "learning to be a good man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E67")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1E67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE7")
    OP_A2(0x4)

    ChrTalk(    #95
        0xFE,
        (
            "Ruan was originally a town of\x01",
            "sailors and fishermen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "You'd have men from around the\x01",
            "world here and all of 'em made\x01",
            "their living at sea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I want my son to live that kind\x01",
            "of life, too...to be a real man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E67")

    label("loc_1DE7")


    ChrTalk(    #98
        0xFE,
        (
            "Ruan was originally a town of\x01",
            "sailors and fishermen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "I want my son to live that kind\x01",
            "of life, too...to be a real man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E67")

    TalkEnd(0xC)
    Return()

    # Function_8_15FD end

    def Function_9_1E6B(): pass

    label("Function_9_1E6B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1EF8")

    ChrTalk(    #100
        0xFE,
        (
            "This whole mess with the mayor\x01",
            "has caused quite a stir...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "It's making it difficult to study,\x01",
            "what with all the noise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_269F")

    label("loc_1EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_204D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC4")
    OP_A2(0x5)

    ChrTalk(    #102
        0xFE,
        (
            "Ah, yes. Nikita is also a student\x01",
            "at the royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Perhaps I should ask her what\x01",
            "kind of tests she's had to deal\x01",
            "with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "I'd hate to have to ask the lady\x01",
            "next door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204A")

    label("loc_1FC4")


    ChrTalk(    #105
        0xFE,
        (
            "Ah, yes. Nikita is also a student\x01",
            "at the royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Perhaps I should ask her what\x01",
            "kind of tests she's had to deal\x01",
            "with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204A")

    Jump("loc_269F")

    label("loc_204D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_221C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218A")
    OP_A2(0x5)

    ChrTalk(    #107
        0xFE,
        (
            "I went to go check out the Royal\x01",
            "Academy. It was just what you'd\x01",
            "expect from such a famous school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "I'd heard about the festival,\x01",
            "but I was impressed with just\x01",
            "how much thought went into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "I really want to have Antonio get\x01",
            "into that school. They just have\x01",
            "such charming uniforms!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2219")

    label("loc_218A")


    ChrTalk(    #110
        0xFE,
        (
            "I went to go check out the\x01",
            "royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "I really want to have Antonio get\x01",
            "into that school. They just have\x01",
            "such charming uniforms!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2219")

    Jump("loc_269F")

    label("loc_221C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_237F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E5")
    OP_A2(0x5)

    ChrTalk(    #112
        0xFE,
        (
            "The royal academy's campus\x01",
            "festival is coming up fast!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Now's the perfect opportunity\x01",
            "for us to check it out for my\x01",
            "son's future education.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "I have to take him there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_237C")

    label("loc_22E5")


    ChrTalk(    #115
        0xFE,
        (
            "The royal academy's campus\x01",
            "festival is coming up fast!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Now's the perfect opportunity \x01",
            "to check out the school for\x01",
            "my son's future education.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_237C")

    Jump("loc_269F")

    label("loc_237F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2434")

    ChrTalk(    #117
        0xFE,
        (
            "The royal academy has more\x01",
            "applicants with each year that\x01",
            "passes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "That's why the entrance\x01",
            "examination can be so\x01",
            "difficult to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "This makes me nervous...\x02",
    )

    CloseMessageWindow()
    Jump("loc_269F")

    label("loc_2434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_24D7")

    ChrTalk(    #120
        0xFE,
        (
            "The royal academy's entrance\x01",
            "exam is apparently as difficult\x01",
            "as I'd heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "It might take a lot more \x01",
            "dedication than Sunday\x01",
            "School ever did...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_269F")

    label("loc_24D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_2612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25BB")
    OP_A2(0x5)

    ChrTalk(    #122
        0xFE,
        (
            "Someone as old as my dad would\x01",
            "probably just get left behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "I don't think he could make it\x01",
            "in school nowadays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Our neighbor, Gerome, also\x01",
            "attends the Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "My son won't lose to him!\x02",
    )

    CloseMessageWindow()
    Jump("loc_260F")

    label("loc_25BB")


    ChrTalk(    #126
        0xFE,
        (
            "Our neighbor, Gerome, also\x01",
            "attends the Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "My son won't lose to him!\x02",
    )

    CloseMessageWindow()

    label("loc_260F")

    Jump("loc_269F")

    label("loc_2612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_269F")
    TurnDirection(0xFE, 0x136, 0)

    ChrTalk(    #128
        0xFE,
        (
            "Hey, I know that uniform...\x01",
            "Are you a royal academy student?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Now that I get a close look at it,\x01",
            "I like it even more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269F")

    TalkEnd(0xD)
    Return()

    # Function_9_1E6B end

    def Function_10_26A3(): pass

    label("Function_10_26A3")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26ED")

    ChrTalk(    #130
        0xFE,
        (
            "I wonder what our dads were\x01",
            "making so much noise about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB2")

    label("loc_26ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_279C")

    ChrTalk(    #131
        0xFE,
        (
            "I think that studying natural\x01",
            "science has a lot to do with\x01",
            "my dream of crewing a ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "I've just got to try my hardest\x01",
            "on the royal academy\x01",
            "entrance exam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB2")

    label("loc_279C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2838")

    ChrTalk(    #133
        0xFE,
        (
            "I went to the royal academy\x01",
            "campus festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "I didn't really go to check out\x01",
            "the usual class routine, but I\x01",
            "like the feel of the place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB2")

    label("loc_2838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28FC")
    OP_A2(0x6)

    ChrTalk(    #135
        0xFE,
        (
            "Can't hurt to go take a\x01",
            "look at the campus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I haven't decided to go yet,\x01",
            "though, so I haven't taken\x01",
            "the entrance exam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "I don't want my mom to get\x01",
            "her hopes up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_292D")

    label("loc_28FC")


    ChrTalk(    #138
        0xFE,
        (
            "Can't hurt to go take a\x01",
            "look at the campus.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_292D")

    Jump("loc_2DB2")

    label("loc_2930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2AAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A29")
    OP_A2(0x6)

    ChrTalk(    #139
        0xFE,
        (
            "My dad says I should think\x01",
            "about things carefully before\x01",
            "I decide what I want to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "That's why I think I need to\x01",
            "study a lot in order to crew\x01",
            "an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "I don't think attending school\x01",
            "would be such a bad thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AA8")

    label("loc_2A29")


    ChrTalk(    #142
        0xFE,
        (
            "I think I need to study a lot\x01",
            "in order to crew an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "I don't think attending school\x01",
            "would be such a bad thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA8")

    Jump("loc_2DB2")

    label("loc_2AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2BFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7D")
    OP_A2(0x6)

    ChrTalk(    #144
        0xFE,
        (
            "I want to eventually work as\x01",
            "a crewman, aboard an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "It's what I've wanted to do,\x01",
            "ever since I was a little kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "And that's never changed,\x01",
            "even once, in all that time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF9")

    label("loc_2B7D")


    ChrTalk(    #147
        0xFE,
        (
            "I want to eventually work as\x01",
            "a crewman, aboard an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "And that's never changed,\x01",
            "even once, in all that time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF9")

    Jump("loc_2DB2")

    label("loc_2BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_2D55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFC")
    OP_A2(0x6)

    ChrTalk(    #149
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "My father encourages me to\x01",
            "become an airship crewman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "...but my mom won't shut\x01",
            "up about me going to the\x01",
            "Jenis Royal Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "I really don't think that going\x01",
            "to college is a big deal, for\x01",
            "what I want to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D52")

    label("loc_2CFC")


    ChrTalk(    #153
        0xFE,
        (
            "I really don't think that going\x01",
            "to college is a big deal, for\x01",
            "what I want to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D52")

    Jump("loc_2DB2")

    label("loc_2D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2DB2")

    ChrTalk(    #154
        0xFE,
        (
            "I should head over to the\x01",
            "harbor soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "There are things I want to\x01",
            "get done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB2")

    TalkEnd(0xE)
    Return()

    # Function_10_26A3 end

    def Function_11_2DB6(): pass

    label("Function_11_2DB6")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E4F")
    OP_A2(0x7)

    ChrTalk(    #156
        0xFE,
        (
            "Okay, I need to head over\x01",
            "to the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "*sigh* As harbormaster, I should\x01",
            "definitely not have to put up\x01",
            "with such nonsense...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA9")

    label("loc_2E4F")


    ChrTalk(    #158
        0xFE,
        (
            "*sigh* As harbormaster, I should\x01",
            "definitely not have to put up\x01",
            "with such nonsense...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA9")

    TalkEnd(0xF)
    Return()

    # Function_11_2DB6 end

    def Function_12_2EAD(): pass

    label("Function_12_2EAD")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_306F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE6")
    OP_A2(0x8)

    ChrTalk(    #159
        0xFE,
        (
            "No one except the Dalmores \x01",
            "have ever been elected as\x01",
            "mayor before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "But the next election will change\x01",
            "all of that, unpleasant though it\x01",
            "will be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "I guess that if anyone else\x01",
            "wants to be mayor, now's\x01",
            "the time to go after it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "...I wish my husband had a\x01",
            "little more drive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306C")

    label("loc_2FE6")


    ChrTalk(    #163
        0xFE,
        (
            "I guess that if anyone else\x01",
            "wants to be mayor, now's\x01",
            "the time to go after it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "...I wish my husband had a\x01",
            "little more drive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306C")

    Jump("loc_35D4")

    label("loc_306F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_3265")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D6")
    OP_A2(0x8)

    ChrTalk(    #165
        0xFE,
        (
            "My husband is constantly\x01",
            "worried these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "If he doesn't do something\x01",
            "about it soon, he'll wind up\x01",
            "completely at his wit's end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "I think my son should put a\x01",
            "little more pressure on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "I don't think he knows what\x01",
            "he really wants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "This constant tug-of-war\x01",
            "between the two of them is\x01",
            "really getting on my nerves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3262")

    label("loc_31D6")


    ChrTalk(    #170
        0xFE,
        (
            "My husband is constantly\x01",
            "worried these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "If he doesn't do something\x01",
            "about it soon, he'll wind up\x01",
            "completely at his wit's end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3262")

    Jump("loc_35D4")

    label("loc_3265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_33EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_335A")
    OP_A2(0x8)

    ChrTalk(    #172
        0xFE,
        (
            "My son's campus festival is\x01",
            "coming up soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "But...he doesn't much like his\x01",
            "parents being there. I guess\x01",
            "he feels he's too old for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Boys eventually grow into men,\x01",
            "but little girls are much more\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EC")

    label("loc_335A")


    ChrTalk(    #175
        0xFE,
        (
            "My son's campus festival is\x01",
            "coming up soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "But...he doesn't much like his\x01",
            "parents being there. I guess\x01",
            "he feels he's too old for it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EC")

    Jump("loc_35D4")

    label("loc_33EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_346D")

    ChrTalk(    #177
        0xFE,
        (
            "Oh, no...I wanted to get the\x01",
            "shopping done before the\x01",
            "bridge was up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "Damn...I completely forgot\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35D4")

    label("loc_346D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FD")
    OP_A2(0x8)

    ChrTalk(    #179
        0xFE,
        (
            "My husband's gone off to work\x01",
            "and my son's at school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "I suppose I should set about\x01",
            "getting the house cleaned up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_353D")

    label("loc_34FD")


    ChrTalk(    #181
        0xFE,
        (
            "I suppose I should set about\x01",
            "getting the house cleaned up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_353D")

    Jump("loc_35D4")

    label("loc_3540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_35D4")

    ChrTalk(    #182
        0xFE,
        (
            "My husband is the harbormaster,\x01",
            "but he's a bit of a coward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "He's popular and reliable,\x01",
            "but I wish he'd be a little\x01",
            "more confident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D4")

    TalkEnd(0x10)
    Return()

    # Function_12_2EAD end

    def Function_13_35D8(): pass

    label("Function_13_35D8")

    TalkBegin(0x11)

    ChrTalk(    #184
        0xFE,
        (
            "My father can be kind of\x01",
            "offensive, which works both to\x01",
            "his advantage and detriment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "My mother doesn't always say\x01",
            "the right things, either...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Return()

    # Function_13_35D8 end

    def Function_14_3677(): pass

    label("Function_14_3677")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_37DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375E")
    OP_A2(0x9)

    ChrTalk(    #186
        0xFE,
        (
            "What's happened is truly a\x01",
            "shame, but we can't afford\x01",
            "to sit and puzzle over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "The mayor made a grave mistake,\x01",
            "but he is the reason that Ruan's\x01",
            "been so successful in its expansion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_37D7")

    label("loc_375E")


    ChrTalk(    #189
        0xFE,
        (
            "The mayor made a grave mistake,\x01",
            "but he is the reason that Ruan's\x01",
            "been so successful in its expansion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    label("loc_37D7")

    Jump("loc_3E4F")

    label("loc_37DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_39C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3906")
    OP_A2(0x9)

    ChrTalk(    #191
        0xFE,
        (
            "The biggest source of the changes\x01",
            "in Ruan has been the proliferation\x01",
            "of airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "When the airships stopped flying\x01",
            "the other day, a lot of folks\x01",
            "canceled their travel plans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "It's already reached a point where\x01",
            "Ruan couldn't exist without those\x01",
            "flying contraptions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C6")

    label("loc_3906")


    ChrTalk(    #194
        0xFE,
        (
            "When the airships stopped flying\x01",
            "the other day, a lot of folks\x01",
            "canceled their travel plans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "It's already reached a point where\x01",
            "Ruan couldn't exist without those\x01",
            "flying contraptions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C6")

    Jump("loc_3E4F")

    label("loc_39C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3A54")

    ChrTalk(    #196
        0xFE,
        (
            "I was thinking of taking a short\x01",
            "vacation when the royal academy's\x01",
            "campus festival rolls around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "Next year, perhaps...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E4F")

    label("loc_3A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B17")
    OP_A2(0x9)

    ChrTalk(    #198
        0xFE,
        (
            "Those little crooks down at\x01",
            "the harbor are the source\x01",
            "of most of my headaches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "They aren't just making things\x01",
            "unpleasant for the occasional\x01",
            "tourist here and there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3F")

    label("loc_3B17")


    ChrTalk(    #200
        0xFE,
        "Those fools are no end of trouble.\x02",
    )

    CloseMessageWindow()

    label("loc_3B3F")

    Jump("loc_3E4F")

    label("loc_3B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C63")
    OP_A2(0x9)

    ChrTalk(    #201
        0xFE,
        (
            "Ruan has been changing into\x01",
            "a real tourist area lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "It presents a real opportunity\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "It means that I'll have customers\x01",
            "from all over Liberl coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "Personally, I see absolutely no\x01",
            "issues with the mayor's plans\x01",
            "for tourist expansion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CCC")

    label("loc_3C63")


    ChrTalk(    #205
        0xFE,
        (
            "Ruan has been changing into\x01",
            "a real tourist area lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "It presents a real opportunity\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CCC")

    Jump("loc_3E4F")

    label("loc_3CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_3E4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DBA")
    OP_A2(0x9)

    ChrTalk(    #207
        0xFE,
        (
            "I work in the tourist and hotel\x01",
            "industries of central Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "The most popular new construction\x01",
            "with the tourists has definitely been\x01",
            "the Hotel Blanche.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "The penthouse suite there\x01",
            "is particularly nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4F")

    label("loc_3DBA")


    ChrTalk(    #210
        0xFE,
        (
            "The most popular new construction\x01",
            "with the tourists has definitely been\x01",
            "the Hotel Blanche.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "The penthouse suite there\x01",
            "is particularly nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E4F")

    TalkEnd(0x12)
    Return()

    # Function_14_3677 end

    def Function_15_3E53(): pass

    label("Function_15_3E53")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3EF1")

    ChrTalk(    #212
        0xFE,
        (
            "I'm in shock that the mayor was\x01",
            "involved in such a horrible scandal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "And I'd thought him to be such\x01",
            "a fine man, when I spoke to him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41CB")

    label("loc_3EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3F58")

    ChrTalk(    #214
        0xFE,
        "I know my husband is busy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "...but I wish he'd spend more\x01",
            "time with our children.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41CB")

    label("loc_3F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3FEA")

    ChrTalk(    #216
        0xFE,
        (
            "I wanted my eldest son to attend\x01",
            "school at the royal academy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "...but what good would it do,\x01",
            "if he doesn't want to go there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41CB")

    label("loc_3FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_40AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4083")
    OP_A2(0xA)

    ChrTalk(    #218
        0xFE,
        "I do have one other son...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "...but circumstances being\x01",
            "what they are, he's not here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "I do hope he's eating all right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40A9")

    label("loc_4083")


    ChrTalk(    #221
        0xFE,
        "I do hope he's eating all right.\x02",
    )

    CloseMessageWindow()

    label("loc_40A9")

    Jump("loc_41CB")

    label("loc_40AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_414D")

    ChrTalk(    #222
        0xFE,
        "Louis can be such a mischievous child.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "It's as if he's never satisfied unless\x01",
            "he tries out every harebrained\x01",
            "notion that pops into his head.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41CB")

    label("loc_414D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_41CB")

    ChrTalk(    #224
        0xFE,
        "My husband truly loves his work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "It's a wonder that he hasn't\x01",
            "passed out from exhaustion\x01",
            "on a few occasions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41CB")

    TalkEnd(0x13)
    Return()

    # Function_15_3E53 end

    def Function_16_41CF(): pass

    label("Function_16_41CF")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4262")

    ChrTalk(    #226
        0xFE,
        (
            "My brother hasn't come home\x01",
            "yet, and my dad said he's\x01",
            "not welcome here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "How come my dad's always\x01",
            "so cold to my big brother?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4437")

    label("loc_4262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_435B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FE")
    OP_A2(0xB)

    ChrTalk(    #228
        0xFE,
        (
            "My brother's probably at\x01",
            "the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "My dad said not to go and\x01",
            "see him, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "Hmph... And my dad never plays\x01",
            "with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4358")

    label("loc_42FE")


    ChrTalk(    #231
        0xFE,
        (
            "My brother's probably at\x01",
            "the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "My dad said not to go and see\x01",
            "him, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4358")

    Jump("loc_4437")

    label("loc_435B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_43A2")

    ChrTalk(    #233
        0xFE,
        (
            "*sigh* I wish my brother would\x01",
            "come and play with me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4437")

    label("loc_43A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_43C2")

    ChrTalk(    #234
        0xFE,
        "Mom, I'm hungry!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4437")

    label("loc_43C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_440A")

    ChrTalk(    #235
        0xFE,
        (
            "My dad was super mad when his\x01",
            "watch broke the other day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4437")

    label("loc_440A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_4437")

    ChrTalk(    #236
        0xFE,
        (
            "My dad's always working.\x01",
            "ALWAYS.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4437")

    TalkEnd(0x14)
    Return()

    # Function_16_41CF end

    SaveToFile()

Try(main)
