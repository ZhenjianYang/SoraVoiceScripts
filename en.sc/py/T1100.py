from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1100   ._SN',
        MapName             = 'Bose',
        Location            = 'T1100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 1,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1100_1 ._SN',
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
        'Marco',                                # 9
        'Monte',                                # 10
        'Fannie',                               # 11
        'Alvelle',                              # 12
        'Simon',                                # 13
        'Royal Army Soldier',                   # 14
        'Rionne',                               # 15
        'Modena',                               # 16
        'New Ansel Path',                       # 17
        'Bose - North Block',                   # 18
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01050 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
        'ED6_DT07/CH01690 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT26/CH20311 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01050P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
        'ED6_DT07/CH01690P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT26/CH20311P._CP',             # 08
    )

    DeclNpc(
        X                   = 50000,
        Z                   = -3000,
        Y                   = 31800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 50000,
        Z                   = -3000,
        Y                   = 30480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 51870,
        Z                   = -3000,
        Y                   = 30650,
        Direction           = 43,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 52830,
        Z                   = -3000,
        Y                   = 32950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 51780,
        Z                   = -3000,
        Y                   = 32900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 44410,
        Z                   = -3000,
        Y                   = 20760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44380,
        Z                   = -3000,
        Y                   = 29520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 43530,
        Z                   = -3000,
        Y                   = 30940,
        Direction           = 122,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 47970,
        Z                   = -3000,
        Y                   = 4220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48070,
        Z                   = 0,
        Y                   = 48590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 53090,
        Y                   = -3000,
        Z                   = 20940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 55320,
        Y                   = -3000,
        Z                   = 33040,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = 65140,
        TriggerZ            = 3000,
        TriggerY            = 36680,
        TriggerRange        = 1000,
        ActorX              = 65280,
        ActorZ              = 5000,
        ActorY              = 36680,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_296",          # 00, 0
        "Function_1_326",          # 01, 1
        "Function_2_395",          # 02, 2
        "Function_3_42A",          # 03, 3
        "Function_4_515",          # 04, 4
        "Function_5_6A5",          # 05, 5
        "Function_6_C93",          # 06, 6
        "Function_7_119B",         # 07, 7
        "Function_8_12E2",         # 08, 8
        "Function_9_1407",         # 09, 9
        "Function_10_1547",        # 0A, 10
        "Function_11_1764",        # 0B, 11
        "Function_12_1ED3",        # 0C, 12
        "Function_13_1ED7",        # 0D, 13
    )


    def Function_0_296(): pass

    label("Function_0_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2BD")
    ClearChrFlags(0xA, 0x80)

    label("loc_2BD")

    Jump("loc_325")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2DE")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_325")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2ED")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_325")

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2FC")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_325")

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_325")
    SetChrPos(0x8, 50940, -3000, 31530, 0)
    SetChrPos(0x9, 49760, -3000, 30480, 0)

    label("loc_325")

    Return()

    # Function_0_296 end

    def Function_1_326(): pass

    label("Function_1_326")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFE7960, 0x230040)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_342")
    Jump("loc_35B")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_35B")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x1)
    OP_10(0x11, 0x1)

    label("loc_35B")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37E")
    OP_65(0x0, 0x1)

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38F")
    OP_1B(0xD, 0x0, 0xB)

    label("loc_38F")

    OP_71(0x12, 0x2)
    Return()

    # Function_1_326 end

    def Function_2_395(): pass

    label("Function_2_395")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_426")

    ChrTalk(    #0
        0xFE,
        (
            "I'm off to the place Borden's wife is\x01",
            "running in the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "They're back in business, after all!\x01",
            "I need to show my support!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426")

    TalkEnd(0xF)
    Return()

    # Function_2_395 end

    def Function_3_42A(): pass

    label("Function_3_42A")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_511")

    ChrTalk(    #2
        0xFE,
        (
            "Things are finally peaceful again,\x01",
            "thank Aidios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "The airships have begun running again,\x01",
            "and now the merchants can really get to\x01",
            "business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "It's easy to forget how complicated it\x01",
            "all is when you're shopping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_511")

    TalkEnd(0xE)
    Return()

    # Function_3_42A end

    def Function_4_515(): pass

    label("Function_4_515")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_606")

    ChrTalk(    #5
        0xFE,
        (
            "The Air Force actually let the dragon\x01",
            "get away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Hard to keep a good face forward as a\x01",
            "soldier after our grand plan fell right\x01",
            "on its ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "A failure like that even gets to you as\x01",
            "a 'lowly ground worm,' you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_6A1")

    ChrTalk(    #8
        0xFE,
        (
            "The brass seems really shaken by\x01",
            "this dragon mess, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "This really has to be a big deal if\x01",
            "they're sending out so much of the\x01",
            "Air Force!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A1")

    TalkEnd(0xFE)
    Return()

    # Function_4_515 end

    def Function_5_6A5(): pass

    label("Function_5_6A5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_751")

    ChrTalk(    #10
        0xFE,
        (
            "The merchants are being very cautious,\x01",
            "and I still have no contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I know they do not wish to act while\x01",
            "airships are still grounded, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BD")

    label("loc_751")


    ChrTalk(    #12
        0xFE,
        (
            "Blast it all. I've visited a number of\x01",
            "merchants I've dealt with in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Every one of them is being cautious in\x01",
            "their dealings. I still have no contract!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I know they do not wish to act while\x01",
            "airships are still grounded, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Nnngh, damn it all! If I cannot make any\x01",
            "deals, there was no point in coming to\x01",
            "this backwater of a kingdom!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8BD")

    Jump("loc_C8F")

    label("loc_8C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_9B6")

    ChrTalk(    #16
        0xFE,
        (
            "The Liberlian Army is seemingly going\x01",
            "to act in response to the...incident at\x01",
            "the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I worry, however. Bose is so close to\x01",
            "Erebonia's southern march...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I hope certain fools back home do\x01",
            "not take this as provocation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8F")

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_AD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A18")

    ChrTalk(    #19
        0xFE,
        (
            "There's some sort of trouble at the market\x01",
            "in the northern block, it seems.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0")

    label("loc_A18")


    ChrTalk(    #20
        0xFE,
        (
            "There's some sort of trouble at the market\x01",
            "in the northern block, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "And the timing could not be worse!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Just as I was about to go work\x01",
            "out some trade deals...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_AD0")

    Jump("loc_C8F")

    label("loc_AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B95")

    ChrTalk(    #23
        0xFE,
        (
            "I must admit, I became fairly lost\x01",
            "the first time I visited this city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Of course, as fate and chance have led me\x01",
            "back here, I have gotten used to Bose's\x01",
            "many streets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8F")

    label("loc_B95")


    ChrTalk(    #25
        0xFE,
        (
            "I must admit, I became fairly lost the\x01",
            "first time I visited this city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Of course, as fate and chance have led me\x01",
            "back here, I have gotten used to Bose's\x01",
            "many streets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "So! First, the shops in the southern block,\x01",
            "and then the market.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C8F")

    TalkEnd(0x8)
    Return()

    # Function_5_6A5 end

    def Function_6_C93(): pass

    label("Function_6_C93")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CE0")

    ChrTalk(    #28
        0xFE,
        (
            "Oh, I give up!\x01",
            "I can't make a deal to save my life!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7A")

    label("loc_CE0")


    ChrTalk(    #29
        0xFE,
        (
            "Oh, I give up! I can't seem to make\x01",
            "any deals, no matter what I do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I just need to accept the fact that\x01",
            "I came at the worst possible time...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D7A")

    Jump("loc_1197")

    label("loc_D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E22")

    ChrTalk(    #31
        0xFE,
        (
            "The Empire's been ordering fewer\x01",
            "and fewer parts for tanks, recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I suppose it makes sense when you\x01",
            "consider the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F20")

    label("loc_E22")


    ChrTalk(    #33
        0xFE,
        (
            "The Empire's been ordering fewer\x01",
            "and fewer parts for tanks, recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I suppose it makes sense when you\x01",
            "consider the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Leaves me feeling a little torn.\x01",
            "I don't want to be a merchant of death,\x01",
            "but it WAS good money...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F20")

    Jump("loc_1197")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_F78")

    ChrTalk(    #36
        0xFE,
        "The market is in chaos...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Not exactly a good time to make deals!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1197")

    label("loc_F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1014")

    ChrTalk(    #38
        0xFE,
        (
            "This city's quite a bit more developed\x01",
            "than I expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Granted, it's still small compared to the\x01",
            "grand cities back in Erebonia.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1197")

    label("loc_1014")


    ChrTalk(    #40
        0xFE,
        (
            "As a merchant of the Empire, or one in\x01",
            "training, at least, I thought I'd try to\x01",
            "increase foreign trade a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "So I thought, 'let's get dangerous!' and\x01",
            "came down here to Liberl to try and\x01",
            "make it happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Thanks to Marco, my mentor, I've managed\x01",
            "to get in touch with several local merchants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Now I just need to work out some good\x01",
            "deals--sooner rather than later!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1197")

    TalkEnd(0x9)
    Return()

    # Function_6_C93 end

    def Function_7_119B(): pass

    label("Function_7_119B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126F")

    ChrTalk(    #44
        0xFE,
        (
            "This workshop is so crowded!\x01",
            "I'm sure they're looking for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I bet if I ask the owner,\x01",
            "I could get a job here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "It's SO crowded, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "No, I must stick it out! For a job!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_12DE")

    label("loc_126F")


    ChrTalk(    #48
        0xFE,
        "There's a lot of people at this workshop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I bet they don't have enough help.\x01",
            "I wonder if I should...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DE")

    TalkEnd(0xA)
    Return()

    # Function_7_119B end

    def Function_8_12E2(): pass

    label("Function_8_12E2")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1367")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FB")
    Call(0, 10)
    Jump("loc_1364")

    label("loc_12FB")


    ChrTalk(    #50
        0xFE,
        (
            "I wonder what's taking that customer\x01",
            "so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "It's been a while since they went into\x01",
            "the shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1364")

    Jump("loc_1403")

    label("loc_1367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1403")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1387")
    Call(0, 10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_1403")

    label("loc_1387")


    ChrTalk(    #52
        0xFE,
        (
            "My family was freaking out last night,\x01",
            "let me tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I can understand why the factory is\x01",
            "so chaotic right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1403")

    TalkEnd(0xB)
    Return()

    # Function_8_12E2 end

    def Function_9_1407(): pass

    label("Function_9_1407")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_148F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1420")
    Call(0, 10)
    Jump("loc_148C")

    label("loc_1420")


    ChrTalk(    #54
        0xFE,
        "Finally about to get in there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "They should be done talking to the\x01",
            "person who went in ahead of me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148C")

    Jump("loc_1543")

    label("loc_148F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1543")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AF")
    Call(0, 10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_1543")

    label("loc_14AF")


    ChrTalk(    #56
        0xFE,
        (
            "Everyone's being hit hard by this...\x01",
            "whatever the hell it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Even Trino spent the night turning his\x01",
            "house upside-down looking for lamps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1543")

    TalkEnd(0xC)
    Return()

    # Function_9_1407 end

    def Function_10_1547(): pass

    label("Function_10_1547")

    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_169B")

    ChrTalk(    #58
        0xC,
        "That reminds me, Alvelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xC,
        (
            "You said you wanted to attend\x01",
            "the royal academy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xB,
        (
            "Yeah, I'm in the middle of studying\x01",
            "for the entrance exams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        (
            "Of course, with the WORLD ENDING or whatever,\x01",
            "it's kind of hard to keep that up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xC,
        "No kidding...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xC,
        (
            "Hard to do anything with anything\x01",
            "orbal not working.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1755")

    label("loc_169B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1755")

    ChrTalk(    #64
        0xB,
        "Oh, Simon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        "You need something from the workshop too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xC,
        "Yeah, Mirano told me to stop by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        "Dad asked me to come, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "Guess everyone's kind of losing it,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1755")

    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_A2(0x3)
    OP_A2(0x4)
    Return()

    # Function_10_1547 end

    def Function_11_1764(): pass

    label("Function_11_1764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_191B")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FF")

    ChrTalk(    #69
        0x108,
        (
            "#074FI'm not sure we have a lot of time to\x01",
            "wander about.\x02\x03",

            "#070FWe should get what we need and\x01",
            "head for the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A7")

    label("loc_17FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1815")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_181C")

    label("loc_1815")

    TurnDirection(0x103, 0x0, 400)

    label("loc_181C")


    ChrTalk(    #70
        0x103,
        (
            "#020FWe are rather on the clock this time,\x01",
            "Estelle.\x02\x03",

            "Once we've picked up anything we need,\x01",
            "we really should get to the landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A7")

    Fade(1000)
    OP_59()
    SetChrPos(0x101, 47790, -3000, 17080, 0)
    SetChrPos(0x103, 47790, -3000, 17080, 0)
    SetChrPos(0x108, 47790, -3000, 17080, 0)
    SetChrPos(0x105, 47790, -3000, 17080, 0)
    SetChrPos(0x104, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_8C(0x0, 0, 0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1ED2")

    label("loc_191B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BF0")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_1949"),
        (2, "loc_1999"),
        (4, "loc_1A0B"),
        (3, "loc_1A69"),
        (6, "loc_1AEF"),
        (7, "loc_1B4A"),
        (SWITCH_DEFAULT, "loc_1B94"),
    )


    label("loc_1949")


    ChrTalk(    #71
        0x101,
        (
            "#1002FWe don't have time to waste!\x02\x03",

            "We need to get to Ravennue, pronto!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B94")

    label("loc_1999")


    ChrTalk(    #72
        0x103,
        (
            "#022FThis is not the time to be wandering\x01",
            "around.\x02\x03",

            "We need to get to Ravennue as\x01",
            "soon as we possibly can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B94")

    label("loc_1A0B")


    ChrTalk(    #73
        0x105,
        (
            "#042FThis is no time for detours.\x02\x03",

            "We must go to Ravennue as soon\x01",
            "as we are prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B94")

    label("loc_1A69")


    ChrTalk(    #74
        0x104,
        (
            "#032FThe stage is aflame, and we must not dally.\x02\x03",

            "We must proceed with haste to Ravennue,\x01",
            "for the next scene awaits us there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B94")

    label("loc_1AEF")


    ChrTalk(    #75
        0x107,
        (
            "#062FWe can't waste time here!\x01",
            "At all!\x02\x03",

            "We need to follow Agate as soon as we can!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B94")

    label("loc_1B4A")


    ChrTalk(    #76
        0x108,
        (
            "#072FThis is no time to wander.\x02\x03",

            "We must get to Ravennue quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B94")

    label("loc_1B94")

    Fade(1000)
    OP_59()
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    SetChrPos(0x3, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1ED2")

    label("loc_1BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED2")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_1C1E"),
        (2, "loc_1C73"),
        (4, "loc_1CCB"),
        (3, "loc_1D19"),
        (6, "loc_1D8D"),
        (7, "loc_1E1C"),
        (SWITCH_DEFAULT, "loc_1E79"),
    )


    label("loc_1C1E")


    ChrTalk(    #77
        0x101,
        (
            "#1002FWe need to get to Ravennue, pronto...\x02\x03",

            "Let's go through the west gate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1C73")


    ChrTalk(    #78
        0x103,
        (
            "#022FThe fastest way to Ravennue will be\x01",
            "through the west gate.\x02\x03",

            "We must hurry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1CCB")


    ChrTalk(    #79
        0x105,
        (
            "#042FRavennue is to the west of Bose.\x02\x03",

            "Let us leave by the west gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1D19")


    ChrTalk(    #80
        0x104,
        (
            "#032FRavennue lies to the west of this\x01",
            "fair city.\x02\x03",

            "The fastest way there would be through\x01",
            "the western gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1D8D")


    ChrTalk(    #81
        0x107,
        (
            "#065FUm, um, um, if we're going to Ravennue,\x01",
            "the west gate would be fastest!\x02\x03",

            "#062FCome on, let's go! We need to catch\x01",
            "up to Agate...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1E1C")


    ChrTalk(    #82
        0x108,
        (
            "#072FThe shortest path to Ravennue lies out\x01",
            "of the western gate.\x02\x03",

            "Let us make haste!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E79")

    label("loc_1E79")

    Fade(1000)
    OP_59()
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    SetChrPos(0x3, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)

    label("loc_1ED2")

    Return()

    # Function_11_1764 end

    def Function_12_1ED3(): pass

    label("Function_12_1ED3")

    SetPlaceName(0x22)
    Return()

    # Function_12_1ED3 end

    def Function_13_1ED7(): pass

    label("Function_13_1ED7")

    SetPlaceName(0x24)
    Return()

    # Function_13_1ED7 end

    SaveToFile()

Try(main)
