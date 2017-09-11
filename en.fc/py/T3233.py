from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3233   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3233.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Percy',                                # 9
        'Ed',                                   # 10
        'Lynn',                                 # 11
        'Recia',                                # 12
        'Cyril',                                # 13
        'Addy',                                 # 14
        'Lucky',                                # 15
        'Sima',                                 # 16
        'Quantay',                              # 17
        'Seagaro',                              # 18
        'Edel',                                 # 19
        "Estelle's Basket",                     # 20
        "Tita's Basket",                        # 21
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
        'ED6_DT07/CH02300 ._CH',             # 00
        'ED6_DT07/CH02310 ._CH',             # 01
        'ED6_DT07/CH02290 ._CH',             # 02
        'ED6_DT07/CH01040 ._CH',             # 03
        'ED6_DT07/CH01270 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01120 ._CH',             # 07
        'ED6_DT07/CH01130 ._CH',             # 08
        'ED6_DT07/CH01160 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01060 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
        'ED6_DT06/CH20021 ._CH',             # 0E
        'ED6_DT06/CH20145 ._CH',             # 0F
        'ED6_DT06/CH20146 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02300P._CP',             # 00
        'ED6_DT07/CH02310P._CP',             # 01
        'ED6_DT07/CH02290P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01270P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01120P._CP',             # 07
        'ED6_DT07/CH01130P._CP',             # 08
        'ED6_DT07/CH01160P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01060P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
        'ED6_DT06/CH20021P._CP',             # 0E
        'ED6_DT06/CH20145P._CP',             # 0F
        'ED6_DT06/CH20146P._CP',             # 10
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 9,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
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
        Unknown3            = 1245198,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1310734,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -1900,
        TriggerZ            = 0,
        TriggerY            = 5070,
        TriggerRange        = 800,
        ActorX              = -1900,
        ActorZ              = 1000,
        ActorY              = 5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1890,
        TriggerZ            = 0,
        TriggerY            = -4990,
        TriggerRange        = 800,
        ActorX              = -1890,
        ActorZ              = 1000,
        ActorY              = -4990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_31A",          # 00, 0
        "Function_1_3B4",          # 01, 1
        "Function_2_3BF",          # 02, 2
        "Function_3_3D5",          # 03, 3
        "Function_4_433",          # 04, 4
        "Function_5_577",          # 05, 5
        "Function_6_795",          # 06, 6
        "Function_7_79C",          # 07, 7
        "Function_8_7A3",          # 08, 8
        "Function_9_7AA",          # 09, 9
        "Function_10_7B1",         # 0A, 10
        "Function_11_7B8",         # 0B, 11
        "Function_12_7BF",         # 0C, 12
        "Function_13_7C6",         # 0D, 13
        "Function_14_7CD",         # 0E, 14
        "Function_15_1F28",        # 0F, 15
        "Function_16_1FC8",        # 10, 16
    )


    def Function_0_31A(): pass

    label("Function_0_31A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_324")
    Jump("loc_3B3")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_32E")
    Jump("loc_3B3")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_34E")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1080, 0, 440, 85)
    Jump("loc_3B3")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_36E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1090, 0, -900, 82)
    Jump("loc_3B3")

    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_378")
    Jump("loc_3B3")

    label("loc_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_382")
    Jump("loc_3B3")

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_38C")
    Jump("loc_3B3")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_396")
    Jump("loc_3B3")

    label("loc_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B3")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1090, 0, -900, 82)

    label("loc_3B3")

    Return()

    # Function_0_31A end

    def Function_1_3B4(): pass

    label("Function_1_3B4")

    OP_72(0x8, 0x10)
    OP_72(0x9, 0x10)
    Return()

    # Function_1_3B4 end

    def Function_2_3BF(): pass

    label("Function_2_3BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3BF")

    label("loc_3D4")

    Return()

    # Function_2_3BF end

    def Function_3_3D5(): pass

    label("Function_3_3D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3E2")
    Jump("loc_42F")

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3EC")
    Jump("loc_42F")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3F6")
    Jump("loc_42F")

    label("loc_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_400")
    Jump("loc_42F")

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_40A")
    Jump("loc_42F")

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_414")
    Jump("loc_42F")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_41E")
    Jump("loc_42F")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_428")
    Jump("loc_42F")

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42F")

    label("loc_42F")

    TalkEnd(0xFE)
    Return()

    # Function_3_3D5 end

    def Function_4_433(): pass

    label("Function_4_433")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_440")
    Jump("loc_573")

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_44A")
    Jump("loc_573")

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4C6")

    ChrTalk(    #0
        0xFE,
        (
            "I heard there was quite a\x01",
            "dangerous incident in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "It's a good thing we decided\x01",
            "to come here early.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_573")

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4D0")
    Jump("loc_573")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_54E")

    ChrTalk(    #2
        0xFE,
        (
            "That was a wonderful bath!\x01",
            "It really warms you up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I feel like I can forget everything\x01",
            "when I'm in there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_573")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_558")
    Jump("loc_573")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_562")
    Jump("loc_573")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_56C")
    Jump("loc_573")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_573")

    label("loc_573")

    TalkEnd(0xFE)
    Return()

    # Function_4_433 end

    def Function_5_577(): pass

    label("Function_5_577")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_584")
    Jump("loc_791")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_58E")
    Jump("loc_791")

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_598")
    Jump("loc_791")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_6C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_608")

    ChrTalk(    #4
        0xFE,
        "I see...lake fishing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "When I get back to the Fisherman's\x01",
            "Guild, I'll check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE")

    label("loc_608")

    OP_A2(0x1)

    ChrTalk(    #6
        0xFE,
        (
            "Nothing like an early morning\x01",
            "bath, is there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "This bath is huge.\x01",
            "It's almost like a lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Hmm... A lake...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Yeah. Lake fishing...\x01",
            "That sounds like it'd be fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE")

    Jump("loc_791")

    label("loc_6C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_6CB")
    Jump("loc_791")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_6D5")
    Jump("loc_791")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_6DF")
    Jump("loc_791")

    label("loc_6DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6E9")
    Jump("loc_791")

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_791")

    ChrTalk(    #10
        0xFE,
        (
            "Yeah, the real charm of a hot\x01",
            "spring is using it in the middle\x01",
            "of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Ah, there isn't anything like the\x01",
            "wind on your skin after a nice,\x01",
            "hot bath.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_791")

    TalkEnd(0xFE)
    Return()

    # Function_5_577 end

    def Function_6_795(): pass

    label("Function_6_795")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_795 end

    def Function_7_79C(): pass

    label("Function_7_79C")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_79C end

    def Function_8_7A3(): pass

    label("Function_8_7A3")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_7A3 end

    def Function_9_7AA(): pass

    label("Function_9_7AA")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_7AA end

    def Function_10_7B1(): pass

    label("Function_10_7B1")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_7B1 end

    def Function_11_7B8(): pass

    label("Function_11_7B8")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_7B8 end

    def Function_12_7BF(): pass

    label("Function_12_7BF")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_12_7BF end

    def Function_13_7C6(): pass

    label("Function_13_7C6")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_7C6 end

    def Function_14_7CD(): pass

    label("Function_14_7CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F27")
    EventBegin(0x0)
    OP_A2(0x528)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B5")
    Fade(1000)
    OP_6D(-1360, 0, 5070, 0)
    SetChrPos(0x101, -150, 0, 4200, 270)
    SetChrPos(0x102, -800, 0, 3380, 0)
    SetChrPos(0x107, -580, 0, 5360, 270)
    OP_0D()

    ChrTalk(    #12
        0x101,
        (
            "#000FLet's see... This is the\x01",
            "door to the baths, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x107,
        (
            "#060FYep. This is the women's bath,\x01",
            "and that's the men's.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A1")

    label("loc_8B5")

    Fade(1000)
    OP_6D(-1360, 0, -4840, 0)
    SetChrPos(0x101, -150, 0, -5600, 270)
    SetChrPos(0x102, -800, 0, -6530, 0)
    SetChrPos(0x107, -580, 0, -4450, 270)
    OP_0D()

    ChrTalk(    #14
        0x101,
        (
            "#000FLet's see... This is the\x01",
            "door to the baths, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #15
        0x107,
        (
            "#065FE-Estelle...\x01",
            "This is the men's bath!\x02\x03",

            "We have to go to the\x01",
            "women's bath.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A1")


    ChrTalk(    #16
        0x101,
        (
            "#004FOh, okay.\x01",
            "They're separated.\x02\x03",

            "#001FHa ha. How silly of me. I\x01",
            "need to change my clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#015FAhem!...\x02\x03",

            "#010FI believe this is goodbye,\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #18
        0x101,
        "#001FOkay! Seeya later.♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x107,
        "#560FScuse us!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-32439, 0, 28640, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, -31500, 1300, 29300, 0)
    SetChrPos(0x14, -30300, 1300, 29300, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1500)
    Fade(1000)
    OP_6D(-63400, -750, 28960, 0)
    SetChrPos(0x107, -65290, -550, 25260, 90)
    SetChrPos(0x101, -64140, -550, 26490, 180)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x107, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrChipByIndex(0x101, 15)
    SetChrChipByIndex(0x107, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x107, 0)
    OP_22(0xA2, 0x0, 0x64)
    OP_22(0x1C7, 0x1, 0x64)
    OP_6D(-65690, -750, 27830, 3000)
    Sleep(400)
    OP_99(0x101, 0x0, 0x2, 0x320)
    OP_99(0x101, 0x2, 0x1, 0x320)
    Sleep(400)

    ChrTalk(    #20
        0x101,
        (
            "#378F#2PAhhhh, that feels sooooo good.\x02\x03",

            "Waaaay better than I ever\x01",
            "thought it would.\x02\x03",

            "#443FI'm not like Dorothy, but I\x01",
            "could see getting seriously\x01",
            "addicted to this.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 7)
    Sleep(400)

    ChrTalk(    #21
        0x107,
        (
            "#391F#5PHa ha... I already am.\x02\x03",

            "When I was little, Grandpa used\x01",
            "to always bring me here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 3)
    Sleep(400)

    ChrTalk(    #22
        0x101,
        "#370F#2PAh, okay.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0xC8, 1600, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0x101, 0x3, 0x5, 0x320)
    Sleep(400)

    ChrTalk(    #23
        0x101,
        "#374F#4PHey, where does that door go?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 1)
    Sleep(400)

    ChrTalk(    #24
        0x107,
        (
            "#390F#6POh, that leads to the open-air\x01",
            "bath I was talking about before.\x02\x03",

            "It's huge! I'll bet it could\x01",
            "fit ten people at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#370F#4PWow, cool.\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x5, 0x3, 0x320)
    Sleep(100)
    SetChrSubChip(0x101, 6)
    Sleep(400)

    ChrTalk(    #26
        0x101,
        (
            "#377F#2PWhoooo... I feel like I could\x01",
            "dissolve in this. All this\x01",
            "traveling has worn me OUT.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 7)
    Sleep(400)

    ChrTalk(    #27
        0x107,
        (
            "#390F#5PHave you been doing all\x01",
            "your traveling on foot?\x02\x03",

            "Why not take an airship?\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x3, 0x2, 0x320)
    Sleep(400)

    ChrTalk(    #28
        0x101,
        (
            "#442F#2PUmmm...for training,\x01",
            "I guess.\x02\x03",

            "#442F#2PMy dad always said it\x01",
            "was super-important...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0x7, 0x9, 0x4B0)
    OP_99(0x107, 0x9, 0x7, 0x4B0)
    OP_99(0x107, 0x7, 0x9, 0x4B0)
    OP_99(0x107, 0x9, 0x7, 0x4B0)
    Sleep(400)

    ChrTalk(    #29
        0x107,
        "#393F#5PYou mean Mister Cassius...?\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x2, 0x4, 0x320)
    Sleep(400)

    ChrTalk(    #30
        0x101,
        (
            "#376F#2PYeah... Schera was another student of my\x01",
            "dad's.\x02\x03",

            "He told her all the time that she should travel\x01",
            "by foot.\x02\x03",

            "'You should see the places you should protect\x01",
            "with your own eyes,' or some such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x107,
        "#396F#5PWhoa, cool...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#378F#2PYeah, he was big on impressive\x01",
            "speeches. But he knew how to\x01",
            "back them up when he had to.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x4, 0x3, 0x320)
    Sleep(100)
    SetChrSubChip(0x101, 6)
    Sleep(400)

    ChrTalk(    #33
        0x101,
        "#377F#2P*sigh*... I wonder where he is now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x107,
        "#392F#5PEstelle...\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x3, 0x4, 0x320)
    Sleep(400)

    ChrTalk(    #35
        0x101,
        (
            "#443F#2PHa ha ha... Sorry. Didn't mean\x01",
            "to get all gloomy on you.\x02\x03",

            "#376F#2PI'm in training, too...and\x01",
            "it's not like worrying will\x01",
            "do me any good.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x4, 0x0, 0x3E8)
    Sleep(400)

    ChrTalk(    #36
        0x101,
        (
            "#440F#2PI guess all I can do...\x01",
            "is have faith in him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x107,
        (
            "#393F#5PFaith...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0xC8, 1600, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0x101, 0x0, 0x4, 0x3E8)
    Sleep(400)

    ChrTalk(    #38
        0x101,
        "#370F#2PMm? Something wrong?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 2)
    Sleep(80)
    SetChrSubChip(0x107, 3)
    Sleep(80)
    SetChrSubChip(0x107, 2)
    Sleep(80)
    SetChrSubChip(0x107, 4)
    Sleep(80)
    SetChrSubChip(0x107, 2)
    Sleep(80)
    SetChrSubChip(0x107, 3)
    Sleep(80)
    SetChrSubChip(0x107, 2)
    Sleep(80)
    SetChrSubChip(0x107, 4)
    Sleep(80)
    SetChrSubChip(0x107, 2)
    Sleep(400)

    ChrTalk(    #39
        0x107,
        "#390F#5PNo... No, I'm okay.\x02",
    )

    CloseMessageWindow()
    OP_99(0x107, 0x9, 0x7, 0x320)
    Sleep(400)

    ChrTalk(    #40
        0x107,
        (
            "#396F#5POh, yeah!\x02\x03",

            "I had something I wanted\x01",
            "to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#370F#2PSomething?\x02\x03",

            "#371F#2POkay, dish!\x01",
            "You can ask me anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x107,
        (
            "#395F#5PUm, err, well...\x02\x03",

            "Are you and Joshua married?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#371F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x107,
        "#396F#5P...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x101, 9)
    OP_0D()
    OP_99(0x101, 0x9, 0x7, 0x320)
    Sleep(400)

    ChrTalk(    #45
        0x101,
        (
            "#370F#2PUh, sorry.\x01",
            "I must have spaced out.\x02\x03",

            "What about me and Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0x7, 0x5, 0x320)
    Sleep(400)

    ChrTalk(    #46
        0x107,
        (
            "#397F#5PI...was wondering...if you\x01",
            "and Joshua were married...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #47
        0x101,
        "#374F#2PWha... Wha... Wha...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #48
        0x101,
        (
            "#372F#2P#3SWhy would you ask a thing\x01",
            "like that?!\x02",
        )
    )

    SetChrSubChip(0x101, 10)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_99(0x107, 0x7, 0x9, 0x514)
    OP_99(0x107, 0x9, 0x7, 0x514)
    OP_99(0x107, 0x7, 0x9, 0x514)
    OP_99(0x107, 0x9, 0x7, 0x514)
    Sleep(400)

    ChrTalk(    #49
        0x107,
        (
            "#394F#5PB-But you have the same\x01",
            "last name...\x02\x03",

            "You don't look like each other\x01",
            "at all, so I didn't think you\x01",
            "were siblings...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 11)
    Sleep(400)

    ChrTalk(    #50
        0x101,
        (
            "#444F#2PWe don't look alike because\x01",
            "we're not blood-related!\x02\x03",

            "O-Our names are the same\x01",
            "because Joshua was adopted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x107,
        (
            "#393F#5POhhh, okay...\x02\x03",

            "#395FHee hee, sorry.\x01",
            "I had it all wrong...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 12)
    Sleep(400)

    ChrTalk(    #52
        0x101,
        (
            "#377F#2PB-Boy, did you ever...\x02\x03",

            "Besides, he and I are\x01",
            "both only sixteen.\x02\x03",

            "Marriage is a subject for \x01",
            "waaaayy off in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x107,
        (
            "#395F#5PR-Right...\x02\x03",

            "I guess you wouldn't get married\x01",
            "so young, no matter how much you\x01",
            "love each other, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#377F#2PErk...\x02",
    )

    SetChrSubChip(0x101, 13)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #55
        0x101,
        (
            "#375F#2P#3SI'm telling you, Joshua and I are\x01",
            "not boyfriend and girlfriend!\x02",
        )
    )

    SetChrSubChip(0x101, 14)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#375F#2P#3SWe're just family!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_99(0x107, 0xA, 0xC, 0x3E8)
    OP_99(0x107, 0xC, 0xA, 0x3E8)
    Sleep(400)

    ChrTalk(    #57
        0x107,
        "#394F#5PR-Really?!\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0xE, 0x10, 0x3E8)
    Sleep(400)

    ChrTalk(    #58
        0x101,
        (
            "#377F#2PWhaddya mean, 'Really'?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 11)
    Sleep(400)

    ChrTalk(    #59
        0x101,
        (
            "#444F#2PUh, sweetie...\x02\x03",

            "Do you get that kind of vibe\x01",
            "from watching us, or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x107,
        "#393F#5PWhat kind of vibe?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 17)
    Sleep(400)

    ChrTalk(    #61
        0x101,
        (
            "#441F#2PUh...like we're together.\x01",
            "As in, TOGETHER together.\x02\x03",

            "Like, lovey-dovey, hot,\x01",
            "can't-keep-our-hands-off-\x01",
            "each-other together.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0xB, 0xC, 0x320)
    Sleep(400)

    ChrTalk(    #62
        0x107,
        (
            "#395F#5POh... Well, no...\x02\x03",

            "But, but, you're always with each other, and\x01",
            "you're comfortable with each other, and you\x01",
            "almost finish each other's sentences.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 10)
    Sleep(400)

    ChrTalk(    #63
        0x101,
        (
            "#442F#2PWell, I can't argue with that.\x02\x03",

            "But don't you think that could\x01",
            "just as easily be how family\x01",
            "and close friends act?\x02\x03",

            "And anyway, even if we ever\x01",
            "did feel like that toward each\x01",
            "other...\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x40029, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_AD(0x40027, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_AD(0x4002A, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_AD(0x40028, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_AD(0x4002B, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_AE(0x1F4)
    Sleep(500)
    OP_62(0x101, 0xC8, 1600, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(    #64
        0x101,
        (
            "#375F#2P#3S(Nooooooooooooooooooo!\x01",
            "Bad thoughts! Bad thoughts!)\x02",
        )
    )

    SetChrSubChip(0x101, 19)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrSubChip(0x101, 18)
    Sleep(400)

    ChrTalk(    #65
        0x101,
        (
            "#441F#2P(And why am I getting so embarrassed\x01",
            "by these questions? I always handled\x01",
            "them fine before...)\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0xB, 0xA, 0x320)
    Sleep(400)

    ChrTalk(    #66
        0x107,
        (
            "#393F#5P???\x02\x03",

            "Estelle...?\x01",
            "Your face is all red...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0xC, 0xA, 0x3E8)
    Sleep(400)

    ChrTalk(    #67
        0x101,
        (
            "#378F#2PAck! It's nothing!\x01",
            "No reason at all!\x02\x03",

            "I-I mean, it's because the hot\x01",
            "water's so effective! Yeah!\x02\x03",

            "It just gets the blood going,\x01",
            "and staying in too long can\x01",
            "make you dizzy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x107,
        "#393F#5PO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#371F#2PW-Wasn't there an open-air\x01",
            "bath here?\x02\x03",

            "I suddenly want to try it out!\x01",
            "Let's go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x107,
        "#393F#5PRight...\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xF)
    SetChrSubChip(0x107, 1)
    Sleep(500)

    ChrTalk(    #71
        0x107,
        (
            "#393F#5PBy the way, Estelle...\x01",
            "The open-air bath is...\x02\x03",

            "#394F...unisex.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E86")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_1E86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E99")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_1E99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAC")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_1EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EBF")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_1EBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED2")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_1ED2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE5")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_1EE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EF8")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_1EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0B")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_1F0B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x10000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1F27")

    Return()

    # Function_14_7CD end

    def Function_15_1F28(): pass

    label("Function_15_1F28")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    OP_96(0xFE, 0xFFFF0736, 0x0, 0x6C7A, 0x4B0, 0x1770)
    OP_8E(0xFE, 0xFFFEFE80, 0xFA, 0x7134, 0x1388, 0x0)
    OP_8C(0xFE, 270, 800)
    OP_70(0x6, 0x3C)
    Sleep(60)
    OP_8E(0x101, 0xFFFEF7A0, 0x0, 0x72CE, 0x1388, 0x0)
    Sleep(500)
    OP_72(0x6, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    Return()

    # Function_15_1F28 end

    def Function_16_1FC8(): pass

    label("Function_16_1FC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FE6")
    OP_99(0xFE, 0xE, 0x10, 0x514)
    OP_99(0xFE, 0x10, 0xF, 0x514)
    Jump("Function_16_1FC8")

    label("loc_1FE6")

    Return()

    # Function_16_1FC8 end

    SaveToFile()

Try(main)
