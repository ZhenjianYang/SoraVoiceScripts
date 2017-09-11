from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4211   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4211.x',
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
        'Colonel Richard',                      # 9
        'Captain Amalthea',                     # 10
        'Duke Dunan',                           # 11
        'Butler Phillip',                       # 12
        'Mayor Klaus',                          # 13
        'Dean Collins',                         # 14
        'Factory Chief Murdock',                # 15
        'Lila',                                 # 16
        'Mayor Maybelle',                       # 17
        'Sorella',                              # 18
        'Nage',                                 # 19
        'Primrose',                             # 20
        'Ekle',                                 # 21
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
        'ED6_DT07/CH02030 ._CH',             # 00
        'ED6_DT07/CH02100 ._CH',             # 01
        'ED6_DT07/CH02140 ._CH',             # 02
        'ED6_DT07/CH02470 ._CH',             # 03
        'ED6_DT07/CH02350 ._CH',             # 04
        'ED6_DT07/CH02600 ._CH',             # 05
        'ED6_DT07/CH02620 ._CH',             # 06
        'ED6_DT07/CH02370 ._CH',             # 07
        'ED6_DT07/CH02360 ._CH',             # 08
        'ED6_DT07/CH02460 ._CH',             # 09
        'ED6_DT07/CH02230 ._CH',             # 0A
        'ED6_DT07/CH02240 ._CH',             # 0B
        'ED6_DT07/CH01350 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02030P._CP',             # 00
        'ED6_DT07/CH02100P._CP',             # 01
        'ED6_DT07/CH02140P._CP',             # 02
        'ED6_DT07/CH02470P._CP',             # 03
        'ED6_DT07/CH02350P._CP',             # 04
        'ED6_DT07/CH02600P._CP',             # 05
        'ED6_DT07/CH02620P._CP',             # 06
        'ED6_DT07/CH02370P._CP',             # 07
        'ED6_DT07/CH02360P._CP',             # 08
        'ED6_DT07/CH02460P._CP',             # 09
        'ED6_DT07/CH02230P._CP',             # 0A
        'ED6_DT07/CH02240P._CP',             # 0B
        'ED6_DT07/CH01350P._CP',             # 0C
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        X                   = -1020,
        Z                   = 0,
        Y                   = 85000,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 0,
        Y                   = 76500,
        Direction           = 53,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 0,
        Y                   = 81150,
        Direction           = 255,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -5950,
        Z                   = 0,
        Y                   = 68110,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_36A",          # 01, 1
        "Function_2_374",          # 02, 2
        "Function_3_38A",          # 03, 3
        "Function_4_503",          # 04, 4
        "Function_5_67E",          # 05, 5
        "Function_6_7A5",          # 06, 6
        "Function_7_BAC",          # 07, 7
        "Function_8_392D",         # 08, 8
        "Function_9_3971",         # 09, 9
        "Function_10_39A1",        # 0A, 10
        "Function_11_39F9",        # 0B, 11
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2C0")
    OP_A3(0x3FA)
    Event(0, 7)

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA")
    SetChrChipByIndex(0x0, 9)
    SetChrChipByIndex(0x1, 10)
    SetChrChipByIndex(0x138, 11)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_308")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_369")

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_31C")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_369")

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_33A")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_369")

    label("loc_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_358")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_369")

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_362")
    Jump("loc_369")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_369")

    label("loc_369")

    Return()

    # Function_0_2B2 end

    def Function_1_36A(): pass

    label("Function_1_36A")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_36A end

    def Function_2_374(): pass

    label("Function_2_374")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_389")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_374")

    label("loc_389")

    Return()

    # Function_2_374 end

    def Function_3_38A(): pass

    label("Function_3_38A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_397")
    Jump("loc_4FF")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_410")

    ChrTalk(    #0
        0xFE,
        (
            "The city must be in quite a\x01",
            "state today, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If I didn't have work, I'd love\x01",
            "to go see for myself...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF")

    label("loc_410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_41A")
    Jump("loc_4FF")

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_424")
    Jump("loc_4FF")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_468")

    ChrTalk(    #2
        0xFE,
        (
            "Now where did Shea and Mistress\x01",
            "Hilda get off to...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF")

    label("loc_468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_4FF")

    ChrTalk(    #3
        0xFE,
        (
            "You know why all these guests\x01",
            "are REALLY here? Because the\x01",
            "duke got BORED, that's why!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "That man makes so much work for\x01",
            "me, I swear...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF")

    TalkEnd(0xFE)
    Return()

    # Function_3_38A end

    def Function_4_503(): pass

    label("Function_4_503")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_510")
    Jump("loc_67A")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_51A")
    Jump("loc_67A")

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_524")
    Jump("loc_67A")

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_52E")
    Jump("loc_67A")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_598")

    ChrTalk(    #5
        0xFE,
        (
            "Colonel Richard is such an amazing\x01",
            "man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Pearls before the swine that is\x01",
            "Duke Dunan...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_67A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5F7")

    ChrTalk(    #7
        0xFE,
        (
            "I hate how the duke just stares\x01",
            "menacingly at people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "It's so rude!\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A")

    label("loc_5F7")

    OP_A2(0x2)

    ChrTalk(    #9
        0xFE,
        (
            "I just passed Duke Dunan in the\x01",
            "hall a moment ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I hate how he just stares at\x01",
            "people menacingly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "It's so rude!\x02",
    )

    CloseMessageWindow()

    label("loc_67A")

    TalkEnd(0xFE)
    Return()

    # Function_4_503 end

    def Function_5_67E(): pass

    label("Function_5_67E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_7A1")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_695")
    Jump("loc_7A1")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_7A1")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_6A9")
    Jump("loc_7A1")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(    #12
        0xFE,
        "Finished, at last!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Now to get my cleaning supplies\x01",
            "cleaned up, and get home. Home is\x01",
            "where the lack of cleaning is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A1")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_7A1")

    ChrTalk(    #14
        0xFE,
        "May I...help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I'm sorry to be rude, but I'm\x01",
            "very busy right now preparing\x01",
            "for the banquet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A1")

    TalkEnd(0xFE)
    Return()

    # Function_5_67E end

    def Function_6_7A5(): pass

    label("Function_6_7A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_7B2")
    Jump("loc_BA8")

    label("loc_7B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_84B")

    ChrTalk(    #16
        0xFE,
        (
            "I saw the leader of the Special Ops\x01",
            "without his mask...and let me tell\x01",
            "you, he is one handsome man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "I wonder why he wears it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_900")

    label("loc_84B")


    ChrTalk(    #18
        0xFE,
        (
            "This is just between you and\x01",
            "me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I saw the leader of the Special Ops\x01",
            "without his mask...and let me tell\x01",
            "you, he is one handsome man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "I wonder why he wears it?\x02",
    )

    CloseMessageWindow()

    label("loc_900")

    Jump("loc_BA8")

    label("loc_903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_90D")
    Jump("loc_BA8")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_917")
    Jump("loc_BA8")

    label("loc_917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9AD")

    ChrTalk(    #21
        0xFE,
        (
            "Cleaning up after the duke's\x01",
            "meals is revolting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "It's hard to believe that he,\x01",
            "the queen and the princess are\x01",
            "all related.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5F")

    label("loc_9AD")


    ChrTalk(    #23
        0xFE,
        (
            "This is just between you and\x01",
            "me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Cleaning up after the duke's\x01",
            "meals is revolting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "It's hard to believe that he,\x01",
            "the queen and the princess are\x01",
            "all related.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5F")

    Jump("loc_BA8")

    label("loc_A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_BA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AF7")

    ChrTalk(    #26
        0xFE,
        (
            "He has enough servants, but he\x01",
            "keeps trying to convince Mistress\x01",
            "Hilda to hire on more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "To no good end, either, I'm sure!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA8")

    label("loc_AF7")


    ChrTalk(    #28
        0xFE,
        (
            "This is just between you and\x01",
            "me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "He has enough servants, but he\x01",
            "keeps trying to convince Mistress\x01",
            "Hilda to hire on more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "To no good end, either, I'm sure!\x02",
    )

    CloseMessageWindow()

    label("loc_BA8")

    TalkEnd(0xFE)
    Return()

    # Function_6_7A5 end

    def Function_7_BAC(): pass

    label("Function_7_BAC")

    EventBegin(0x0)
    OP_6D(1430, 30, 80070, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(371, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xC, -2450, 0, 82370, 90)
    SetChrPos(0xD, -2450, 0, 79820, 90)
    SetChrPos(0xE, -2450, 0, 77340, 90)
    SetChrPos(0x10, -2450, 0, 74860, 90)
    SetChrPos(0xF, -3070, 0, 74030, 90)
    SetChrPos(0x108, 2490, 0, 79820, 270)
    SetChrPos(0x102, 2490, 0, 74860, 270)
    SetChrPos(0x101, 2490, 0, 77340, 270)

    ChrTalk(    #31
        0x101,
        (
            "#000FUmm...\x01",
            "This is a dinner party, right?\x02\x03",

            "What's with all the empty plates, then?\x02\x03",

            "Plenty of knives and forks, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#010FThat's because it's a formal dinner.\x02\x03",

            "Everything comes out in a specific\x01",
            "order, starting with hors d'oeuvres.\x02\x03",

            "Then, you use the knives and\x01",
            "forks from the outside in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#000FAnd THAT'S all part of having\x01",
            "good table manners?\x02\x03",

            "Aaaaand here comes the\x01",
            "anxiety attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "#610FHa ha ha...\x01",
            "It's really not so bad.\x02\x03",

            "It does mean that you get to have\x01",
            "some of the finest food available.\x02\x03",

            "Manners and etiquette are secondary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xC,
        (
            "#600FIndeed, indeed.\x02\x03",

            "I'm told that you're acquainted\x01",
            "with everyone who'll be attending.\x02\x03",

            "No need to get stressed out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#000FYeah, I guess that's true. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        "#010FPlease, don't encourage her...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "#610FHa ha ha...\x02\x03",

            "On that note, is the gentleman\x01",
            "accompanying you going to be\x01",
            "okay with a knife and fork?\x02\x03",

            "I'm told that folks from the East\x01",
            "usually eat with chopsticks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x108,
        (
            "#070FYou've done your research.\x02\x03",

            "However, I'm a firm believer in\x01",
            "the 'When in Liberl, do as the\x01",
            "Liberlians do' policy.\x02\x03",

            "I am not especially skilled with them,\x01",
            "but I will use a knife and fork.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        (
            "#610FMy...\x01",
            "How elegantly handled.\x02\x03",

            "I'm impressed. You're as much\x01",
            "a gentleman as you are a martial\x01",
            "arts champion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x108,
        "#070FHa ha ha... You flatter me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#000F(Boy, he really is a complete\x01",
            "sucker for a pretty face.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#010F(I think he's more being polite\x01",
            "than a lech, though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xE,
        (
            "#800FAnyway...\x01",
            "His Grace is really late.\x02\x03",

            "I wonder what he's up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xC,
        (
            "#600FHmm... Indeed.\x02\x03",

            "So, if the seat at head of the\x01",
            "table is for the duke, then who\x01",
            "might that other one be for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        (
            "#780FA fine question...\x02\x03",

            "I think it most likely intended\x01",
            "for Princess Klaudia.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -250, 0, 62670, 0)
    SetChrPos(0x9, 460, 0, 62290, 0)
    SetChrPos(0xA, -110, 0, 64099, 0)
    SetChrPos(0xB, 10, 0, 62670, 0)

    def lambda_13E2():
        OP_6D(370, 0, 72370, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13E2)
    Sleep(1000)

    def lambda_13FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_13FF)

    def lambda_1411():
        OP_8E(0xFE, 0xA, 0x0, 0x10586, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1411)
    WaitChrThread(0xB, 0x1)

    def lambda_1431():
        OP_8E(0xFE, 0xFFFFF772, 0x0, 0x105F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1431)
    WaitChrThread(0xB, 0x1)
    OP_8C(0xB, 0, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #47
        0xB,
        (
            "#720FYour attention, ladies and gentlemen. My\x01",
            "humblest apologies for the long delay.\x02\x03",

            "Presenting His Grace the Duke.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_14DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_14DC)

    def lambda_14EE():
        OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x10DE2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14EE)
    Sleep(300)

    def lambda_150E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_150E)

    def lambda_1520():
        OP_8E(0xFE, 0x438, 0x0, 0x10C3E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1520)
    Sleep(600)

    def lambda_1540():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1540)

    def lambda_1552():
        OP_8E(0xFE, 0x190, 0x0, 0x1070C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1552)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #48
        0xA,
        (
            "#220FWell, then. I must apologize\x01",
            "for making you wait so.\x02\x03",

            "I'm afraid that I was in a\x01",
            "meeting, from which I simply\x01",
            "could not break away.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #49
        0xA,
        (
            "#220FThis gentleman is Colonel Richard,\x01",
            "commanding officer of the royal\x01",
            "Intelligence Division.\x02\x03",

            "I've invited him here, to thank him\x01",
            "for his tireless efforts in helping to\x01",
            "deal with the terrorist situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)

    ChrTalk(    #50
        0x8,
        (
            "#110FIt's a pleasure to meet you all.\x02\x03",

            "I was quite gratified to be\x01",
            "invited to this occasion by\x01",
            "our honorable duke.\x02\x03",

            "I ask that you pardon my uncouth\x01",
            "soldier's uniform and allow me\x01",
            "to sit with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0xA)
    Sleep(300)
    Sleep(100)

    def lambda_17BC():
        OP_6D(330, 60, 81510, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17BC)
    OP_43(0x8, 0x1, 0x0, 0x8)
    Sleep(200)
    OP_43(0xB, 0x1, 0x0, 0xB)
    Sleep(200)
    OP_43(0x9, 0x1, 0x0, 0x9)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #51
        0x101,
        (
            "#000F(You've gotta be kidding...\x01",
            "We're having dinner with HIM?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#010F(I suspected this might happen,\x01",
            "but it's still unnerving.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(50, 1210, 79220, 0)
    OP_67(0, 2920, -10000, 0)
    OP_6B(2090, 0)
    OP_6C(0, 0)
    OP_6E(424, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #53
        0xA,
        (
            "#220FHa ha ha... Excellent, excellent.\x02\x03",

            "What say you, Mayor Maybelle?\x01",
            "What do you think of Grancel\x01",
            "Castle's master chef?\x02\x03",

            "Is his cooking not on par with\x01",
            "that found in Bose's Anterose\x01",
            "Restaurant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#610FYes, it's quite remarkable.\x02\x03",

            "The wine selection also perfectly\x01",
            "complements the meal. I almost\x01",
            "want to try hiring him away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "#220FHa ha ha... You are not the\x01",
            "first to say such things.\x02\x03",

            "And what of you...Zin, wasn't\x01",
            "it? Is the food to your liking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x108,
        (
            "#070FOh, it's excellent.\x02\x03",

            "I don't have the words to describe\x01",
            "the sense of refinement and depth...\x02\x03",

            "I certainly believe I could\x01",
            "develop a real taste for\x01",
            "Liberlian cuisine, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "#220FGood, good.\x01",
            "I'm glad to hear it.\x02\x03",

            "And you, young bracers?\x02\x03",

            "I imagine you've never experienced\x01",
            "such fine food in your life before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#000FIt's extremely delicious.\x02\x03",

            "Far more worthy of being associated with the\x01",
            "royal family than the person who invited us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#220FHa ha ha...\x01",
            "Indeed, it is a genuine treat.\x02\x03",

            "...Hmm?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x102,
        (
            "#010FI-It's certainly delicious food.\x02\x03",

            "And we couldn't miss a chance\x01",
            "to attend so prestigious an\x01",
            "event as this.\x02\x03",

            "Thank you very much for\x01",
            "your gracious invitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        (
            "#220FHa ha ha...\x01",
            "Very kind of you to say so.\x02\x03",

            "I do finally remember what my butler\x01",
            "has been telling me about...\x02\x03",

            "We met before, during the\x01",
            "Ruan incident.\x02\x03",

            "Perhaps our fates are linked\x01",
            "in some bizarre fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#000FY-Yes, sir... Maybe so.\x02\x03",

            "(So he'd forgotten all about us until his\x01",
            "butler reminded him...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#220FCome, let us put social classes\x01",
            "and ranks aside for the evening!\x02\x03",

            "Food is abundant and the wine\x01",
            "flows freely, so enjoy to your\x01",
            "heart's content!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "#110FYour Grace...\x02\x03",

            "If we could, I'd like to do\x01",
            "as we discussed first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xA,
        "#220FAhh, yes! That's a fine idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#220FActually, I have something important\x01",
            "to say to you fine folk who represent\x01",
            "the kingdom...\x02\x03",

            "I use this celebration as the place\x01",
            "to make an important announcement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xC,
        "#600FAn announcement...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xE,
        "#800FAnd what might that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "#220FHmm...\x02\x03",

            "I believe I will allow Colonel\x01",
            "Richard to explain in detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#110F...Thank you.\x02\x03",

            "As you are, no doubt, already\x01",
            "aware, Her Majesty has been\x01",
            "in poor health of late.\x02\x03",

            "However, she has been recovering\x01",
            "and may grace us with a public\x01",
            "appearance soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xC,
        "#600FAhh, that's excellent news.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#610FCould we possibly go and\x01",
            "check in on her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#110FUnfortunately, she does not consider\x01",
            "that to be a wise decision at the moment.\x02\x03",

            "In another two or three days, it seems\x01",
            "likely that the terrorists plaguing the\x01",
            "kingdom will be swept away.\x02\x03",

            "In light of that, the queen's \x01",
            "birthday celebrations will be\x01",
            "held, as originally planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        (
            "#780FHrm... Well, the citizens will surely\x01",
            "be happy to hear this news, as they\x01",
            "have been looking forward to it.\x02\x03",

            "But surely, that is not all\x01",
            "you wish to tell us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        (
            "#800FRight. If that were all, you could\x01",
            "have just sent along a message.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#110FHa ha...\x01",
            "Indeed, you are correct.\x02\x03",

            "Her Majesty is continuing to recover,\x01",
            "as was previously stated. However...\x02\x03",

            "...given the gravity of her condition,\x01",
            "she has also issued a proclamation.\x02\x03",

            "Due to her tenuous health...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#110F...she has stated that she wishes to\x01",
            "abdicate the throne, and turn over royal\x01",
            "authority to her nephew, Duke Dunan.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #78
        0xE,
        "#800FWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        "#610FIs this true?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#000F(Joshua... This is...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        (
            "#010F(Yeah... The conspiracy finally\x01",
            "makes its appearance.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "#220FI was surprised when Her Majesty first broached\x01",
            "the subject as well, but her illness has left\x01",
            "her quite frail.\x02\x03",

            "But it is only natural. She has ruled the kingdom\x01",
            "for forty years, leading it through times of strife\x01",
            "and war...all without a husband, might I add.\x02\x03",

            "Given that, I wish to relieve her of the stress\x01",
            "of her duties following the festival's\x01",
            "successful conclusion.\x02\x03",

            "As the heir to the throne, the\x01",
            "decisions are mine to make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        (
            "#600FHow terrible... Her Majesty's condition\x01",
            "is truly that severe?\x02\x03",

            "I'm ashamed that I've never\x01",
            "noticed any signs, in any of\x01",
            "my annual visits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        (
            "#610FIsn't... Isn't this far too serious\x01",
            "a matter to discuss at what is\x01",
            "supposedly a casual dinner?\x02\x03",

            "Pardon my rudeness, but this all\x01",
            "seems to stretch credulity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        "#220FHmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#110FMayor Maybelle...\x02\x03",

            "Are you saying that you cannot\x01",
            "take His Grace at his word?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10,
        (
            "#610FN-No, nothing of the sort!\x02\x03",

            "I simply mean that, as an elected official,\x01",
            "I don't understand why the successor to the\x01",
            "throne can't be elected in the same fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xE,
        (
            "#800FThat's true...\x02\x03",

            "If possible, I'd like to hear\x01",
            "this directly from Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        "#220FH-Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#110FYour unease is quite understandable.\x02\x03",

            "But we do ask that you try to maintain your\x01",
            "composure and allow us to continue.\x02\x03",

            "As mentioned earlier, I believe Her Majesty\x01",
            "will give a formal announcement herself during\x01",
            "the festival.\x02\x03",

            "Could you be persuaded to shelve your\x01",
            "doubts until then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xE,
        "#800FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#110FThe issue is basically this: Once this\x01",
            "becomes common knowledge, we cannot\x01",
            "know how the citizens will react.\x02\x03",

            "This is why we're telling the leaders\x01",
            "first...to help stave off any chaos\x01",
            "or public disorder before it happens.\x02\x03",

            "This was also the decision\x01",
            "of His Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "#220FAhem!\x01",
            "Well, yes. This is true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#110FAlso, the queen's abdication of\x01",
            "the throne will have international\x01",
            "repercussions.\x02\x03",

            "The other nations on the continent will have\x01",
            "their eyes on us, and we must be watchful for\x01",
            "any action on the part of the Erebonians.\x02\x03",

            "Surely, you can see why it is\x01",
            "necessary to show unified support\x01",
            "for the new king.\x02\x03",

            "This is the world in which we\x01",
            "are going to be living.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(    #95
        0x101,
        "#000F(He makes it all sound so rational...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#010F(Yeah...\x01",
            "He's quite the master manipulator.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE)

    ChrTalk(    #97
        0xE,
        (
            "#800FIn other words, the official decree will\x01",
            "be given during the birthday celebrations...\x02\x03",

            "...but you thought it would be best to inform us\x01",
            "first so that we can be prepared for any issues\x01",
            "that may arise, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#110FHa ha... I'm glad to see that\x01",
            "we have an understanding.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC)

    ChrTalk(    #99
        0xC,
        (
            "#600FHmmm...\x02\x03",

            "If this all comes to pass, we're\x01",
            "going to find ourselves quite busy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10)

    ChrTalk(    #100
        0x10,
        (
            "#610FYes...and we'll have to announce\x01",
            "it to the citizens.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD)

    ChrTalk(    #101
        0xD,
        "#780FI have a question...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xD,
        (
            "#780FI believe that the duke has a\x01",
            "fair claim to the throne...\x02\x03",

            "However, is there not another who also\x01",
            "has the same right of succession?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        "#220FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#110FNo doubt, you're referring to\x01",
            "Her Majesty's granddaughter,\x01",
            "Princess Klaudia.\x02\x03",

            "It is true that she and His Grace have\x01",
            "an equal claim to the throne.\x02\x03",

            "But it would appear that Her Majesty did not\x01",
            "choose her due to her tender age.\x02\x03",

            "And I must say, I agree with her wisdom in\x01",
            "this matter. I should hardly like to impose\x01",
            "such responsibility upon a girl so young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "#220FYes! Yes, absolutely!\x02\x03",

            "For the time being, I believe it would be best\x01",
            "for Klaudia to find a fine marriage prospect.\x02\x03",

            "Though it is strictly informal, there is\x01",
            "already interest from the royal families of\x01",
            "a number of other nations.\x02\x03",

            "Perhaps a royal wedding could take place as\x01",
            "soon as this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        "#610FOh, my...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        (
            "#780FHm... I understand.\x02\x03",

            "If that happens, then we'll have\x01",
            "two major events to celebrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xC,
        (
            "#600FHmm...\x02\x03",

            "I honestly think she's a bit\x01",
            "young for marriage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x108,
        (
            "#070F...'Scuse me.\x01",
            "May I ask a question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#000FZ-Zin...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "#220FHmm?\x02\x03",

            "I don't mind. Speak freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x108,
        (
            "#070FSorry to seem rude, but this doesn't\x01",
            "sound like the kind of conversation\x01",
            "you'd want outsiders hearing.\x02\x03",

            "Particularly a foreigner...\x02\x03",

            "So how come you're making\x01",
            "this announcement now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "#110FThat is solely because of the serendipitous\x01",
            "turn of events that allowed bracers to win\x01",
            "the championship.\x02\x03",

            "We had wanted to inform the guild\x01",
            "of this in advance, as well.\x02\x03",

            "I've already discussed the\x01",
            "idea with Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x108,
        (
            "#070FGot'cha...\x02\x03",

            "I guess Liberl's military and\x01",
            "bracers are on just as good of\x01",
            "terms as the stories say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#110FHa ha... That is because we lack\x01",
            "the military strength of the\x01",
            "Empire or the Republic.\x02\x03",

            "The harsh reality is that keeping\x01",
            "close relations with each other\x01",
            "is a must.\x02\x03",

            "In any event, do you now\x01",
            "understand our intentions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x108,
        (
            "#070FHmm... Yeah, all right.\x02\x03",

            "We'll pass on what we've learned\x01",
            "here to the guild, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4222   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_7_BAC end

    def Function_8_392D(): pass

    label("Function_8_392D")

    OP_8E(0xFE, 0x10D6, 0x0, 0x10FC2, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1176, 0x0, 0x14460, 0xBB8, 0x0)
    OP_8E(0xFE, 0x9F6, 0x0, 0x141B8, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_8_392D end

    def Function_9_3971(): pass

    label("Function_9_3971")

    OP_8E(0xFE, 0x10D6, 0x0, 0x10FC2, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1176, 0x0, 0x14460, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_3971 end

    def Function_10_39A1(): pass

    label("Function_10_39A1")

    OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x117EC, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEF48, 0x0, 0x14D02, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFFBFA, 0x0, 0x14D02, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA, 0x0, 0x14C08, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    Return()

    # Function_10_39A1 end

    def Function_11_39F9(): pass

    label("Function_11_39F9")

    OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x117EC, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEF48, 0x0, 0x14D02, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFFC72, 0x0, 0x15126, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_11_39F9 end

    SaveToFile()

Try(main)
