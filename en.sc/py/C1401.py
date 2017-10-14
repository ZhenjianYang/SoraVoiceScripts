from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1401   ._SN',
        MapName             = 'Bose',
        Location            = 'C1401.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60022",
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
        '',                                     # 9
        'Private Rakel',                        # 10
        'Private Gutte',                        # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
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
        'ED6_DT09/CH11170 ._CH',             # 00
        'ED6_DT09/CH11171 ._CH',             # 01
        'ED6_DT09/CH11180 ._CH',             # 02
        'ED6_DT09/CH11181 ._CH',             # 03
        'ED6_DT09/CH11190 ._CH',             # 04
        'ED6_DT09/CH11191 ._CH',             # 05
        'ED6_DT09/CH10170 ._CH',             # 06
        'ED6_DT09/CH10171 ._CH',             # 07
        'ED6_DT09/CH10840 ._CH',             # 08
        'ED6_DT09/CH10841 ._CH',             # 09
        'ED6_DT07/CH01640 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT09/CH11170P._CP',             # 00
        'ED6_DT09/CH11171P._CP',             # 01
        'ED6_DT09/CH11180P._CP',             # 02
        'ED6_DT09/CH11181P._CP',             # 03
        'ED6_DT09/CH11190P._CP',             # 04
        'ED6_DT09/CH11191P._CP',             # 05
        'ED6_DT09/CH10170P._CP',             # 06
        'ED6_DT09/CH10171P._CP',             # 07
        'ED6_DT09/CH10840P._CP',             # 08
        'ED6_DT09/CH10841P._CP',             # 09
        'ED6_DT07/CH01640P._CP',             # 0A
    )

    DeclNpc(
        X                   = 19810,
        Z                   = 0,
        Y                   = 166800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 860,
        Z                   = -1910,
        Y                   = 188180,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4130,
        Z                   = -1910,
        Y                   = 188050,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclMonster(
        X                   = -31230,
        Z                   = -30,
        Y                   = 76720,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21980,
        Z                   = -30,
        Y                   = 47990,
        Unknown_0C          = 38,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2600,
        Z                   = 10,
        Y                   = 79910,
        Unknown_0C          = 219,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7230,
        Z                   = -1190,
        Y                   = 93200,
        Unknown_0C          = 285,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2350,
        Z                   = -1960,
        Y                   = 58080,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31080,
        Z                   = -1990,
        Y                   = 103160,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4790,
        Z                   = -1950,
        Y                   = 141270,
        Unknown_0C          = 252,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10740,
        Z                   = -2009,
        Y                   = 162000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8460,
        Z                   = -2020,
        Y                   = 79300,
        Unknown_0C          = 280,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21780,
        Z                   = -2050,
        Y                   = 78280,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 920,
        Y                   = -3000,
        Z                   = 189170,
        Range               = 4030,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2E180,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = 19360,
        TriggerZ            = -1990,
        TriggerY            = 166110,
        TriggerRange        = 1000,
        ActorX              = 19810,
        ActorZ              = -490,
        ActorY              = 166800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2BE",          # 00, 0
        "Function_1_2CF",          # 01, 1
        "Function_2_30F",          # 02, 2
        "Function_3_48C",          # 03, 3
        "Function_4_92D",          # 04, 4
        "Function_5_FA8",          # 05, 5
        "Function_6_118B",         # 06, 6
    )


    def Function_0_2BE(): pass

    label("Function_0_2BE")

    OP_11(0xFF, 0xFF, 0xFF, 0x80E8, 0xE290, 0x0)
    Return()

    # Function_0_2BE end

    def Function_1_2CF(): pass

    label("Function_1_2CF")

    OP_C4(0x0, 0x4)
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302")
    OP_6F(0x2, 0)
    Jump("loc_309")

    label("loc_302")

    OP_6F(0x2, 60)

    label("loc_309")

    OP_71(0x1, 0x4)
    Return()

    # Function_1_2CF end

    def Function_2_30F(): pass

    label("Function_2_30F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_334")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_476")

    label("loc_334")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_476")

    label("loc_34D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_476")

    label("loc_366")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_476")

    label("loc_37F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_398")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_476")

    label("loc_398")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_476")

    label("loc_3B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_476")

    label("loc_3CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_476")

    label("loc_3E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FC")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_476")

    label("loc_3FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_476")

    label("loc_415")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_476")

    label("loc_42E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_447")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_476")

    label("loc_447")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_460")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_476")

    label("loc_460")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_476")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_476")

    label("loc_48B")

    Return()

    # Function_2_30F end

    def Function_3_48C(): pass

    label("Function_3_48C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_60C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56F")

    ChrTalk(    #0
        0xFE,
        (
            "Rumor has it that things over at\x01",
            "Haken Gate are a real mess right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Damn gate's stuck wide open,\x01",
            "apparently, and there's no way to\x01",
            "close it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Gonna be fun times for the border\x01",
            "patrol...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_609")

    label("loc_56F")


    ChrTalk(    #3
        0xFE,
        (
            "Rumor has it that things over at\x01",
            "Haken Gate are a real mess right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Damn gate's stuck wide open,\x01",
            "apparently, and there's no way to\x01",
            "close it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_609")

    Jump("loc_929")

    label("loc_60C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_674")

    ChrTalk(    #5
        0xFE,
        (
            "Sorry about this, but I can't let\x01",
            "you go any further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "Turn back, please.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6C0")

    label("loc_674")


    ChrTalk(    #7
        0xFE,
        (
            "Sorry, authorized personnel\x01",
            "only beyond this point. Turn\x01",
            "back, please.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C0")

    Jump("loc_929")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_74F")

    ChrTalk(    #8
        0xFE,
        (
            "I guess we couldn't catch that\x01",
            "dragon in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Hell of a beast, to be able to\x01",
            "evade the entire Royal Army\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_929")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_7D9")

    ChrTalk(    #10
        0xFE,
        (
            "Rumor has it now that\x01",
            "there's a DRAGON around\x01",
            "here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I just hope it decides to stay\x01",
            "the hell away from here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_929")

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_929")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_836")

    ChrTalk(    #12
        0xFE,
        (
            "Sorry, authorized personnel\x01",
            "only beyond this point. Turn\x01",
            "back, please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_929")

    label("loc_836")


    ChrTalk(    #13
        0xFE,
        "Oh, hey! You guys travelers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Sorry about this, but I can't let\x01",
            "you go any further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Ever since the friggin' Capuas stole\x01",
            "back their airship, the patrols been\x01",
            "really cracking down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Please, don't give us any trouble,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_929")

    TalkEnd(0x9)
    Return()

    # Function_3_48C end

    def Function_4_92D(): pass

    label("Function_4_92D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A67")

    ChrTalk(    #17
        0xFE,
        (
            "Man, now we've got a situation over at\x01",
            "Haken Gate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "It's a good thing Her Majesty just signed\x01",
            "that non-aggression pact. Can't imagine\x01",
            "the Empire would try anything now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "But then again, what if this whole thing\x01",
            "was their plan all along? You know, just\x01",
            "to get our guard down?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_B1B")

    label("loc_A67")


    ChrTalk(    #20
        0xFE,
        (
            "Man, now we've got a situation over at\x01",
            "Haken Gate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "It's a good thing Her Majesty just signed\x01",
            "that non-aggression pact. Can't imagine\x01",
            "the Empire would try anything now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1B")

    Jump("loc_FA4")

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD6")

    ChrTalk(    #22
        0xFE,
        (
            "Hey, sorry, folks. This is a Royal\x01",
            "Army training facility. Civilians aren't\x01",
            "allowed to go any further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I'm afraid I'm going to have to ask\x01",
            "you to leave.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_C13")

    label("loc_BD6")


    ChrTalk(    #24
        0xFE,
        (
            "Civilians aren't allowed past\x01",
            "this point. Please leave.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C13")

    Jump("loc_FA4")

    label("loc_C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_D91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CBA")

    ChrTalk(    #25
        0xFE,
        (
            "Not many people come\x01",
            "out here, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I swear, the hardest part of\x01",
            "this job is trying not to fall\x01",
            "asleep while on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "*yaaawn*\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8E")

    label("loc_CBA")


    ChrTalk(    #28
        0xFE,
        (
            "That incident with the ancient dragon's\x01",
            "quieted down by now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I'm grateful for the peace and quiet,\x01",
            "really, but at the same time, I know\x01",
            "it's going to get boring again real soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "*yaaawn*\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D8E")

    Jump("loc_FA4")

    label("loc_D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_E33")

    ChrTalk(    #31
        0xFE,
        (
            "No one's ever clearly\x01",
            "mapped out the western\x01",
            "end of Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "It's a dangerous place to\x01",
            "walk into by mistake, so we\x01",
            "took down the bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA4")

    label("loc_E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_FA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EA6")

    ChrTalk(    #33
        0xFE,
        (
            "Civilians aren't allowed\x01",
            "past this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Sorry, but you're going\x01",
            "to have to turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA4")

    label("loc_EA6")


    ChrTalk(    #35
        0xFE,
        (
            "Ever since those sky bandits broke\x01",
            "in, the brass has really gotten on our\x01",
            "case about our security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Sorry to say, but we really can't let\x01",
            "any civilians past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "The chief's given me strict\x01",
            "orders not to let so much as\x01",
            "a mouse pass through!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FA4")

    TalkEnd(0xA)
    Return()

    # Function_4_92D end

    def Function_5_FA8(): pass

    label("Function_5_FA8")

    OP_EA(0x2, 0x2, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1143")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1092")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_FFF():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FFF)

    def lambda_101A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_101A)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #38
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0xBA, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_106D"),
        (2, "loc_107F"),
        (1, "loc_108F"),
        (SWITCH_DEFAULT, "loc_1092"),
    )


    label("loc_106D")

    OP_A2(0x1B17)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_1092")

    label("loc_107F")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_108F")

    OP_B4(0x0)
    Return()

    label("loc_1092")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A2, 1)"), scpexpr(EXPR_END)), "loc_10DE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #39
        "Found \x1F\xA2\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B16)
    Jump("loc_1140")

    label("loc_10DE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #40
        (
            "Found \x1F\xA2\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xA2\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1140")

    Jump("loc_117D")

    label("loc_1143")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #41
        "\x07\x05Now, now. You know the rules.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_117D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_FA8 end

    def Function_6_118B(): pass

    label("Function_6_118B")

    EventBegin(0x1)
    TurnDirection(0xA, 0x0, 400)

    ChrTalk(    #42
        0xA,
        (
            "Civilians aren't allowed\x01",
            "past this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "Sorry, but you're going\x01",
            "to have to turn back.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8C(0xA, 180, 400)
    Fade(500)
    OP_30(0x1)
    SetMapFlags(0x1)
    OP_0D()
    EventEnd(0x3)
    Return()

    # Function_6_118B end

    SaveToFile()

Try(main)
