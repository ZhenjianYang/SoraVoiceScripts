from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3102   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Passenger',                            # 9
        'Passenger',                            # 10
        'Girl',                                 # 11
        'Female Customer',                      # 12
        'Boy',                                  # 13
        'Passenger',                            # 14
        'Passenger',                            # 15
        'Passenger',                            # 16
        'Gerald',                               # 17
        'Maintenance Chief Gustav',             # 18
        'Bartholomew',                          # 19
        'Cecilia',                              # 20
        'Cecila Shadow',                        # 21
        'Target Camera',                        # 22
        'Zeiss - Factory Block',                # 23
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
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01170 ._CH',             # 02
        'ED6_DT07/CH01130 ._CH',             # 03
        'ED6_DT07/CH01470 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01140 ._CH',             # 0C
        'ED6_DT07/CH01680 ._CH',             # 0D
        'ED6_DT07/CH02440 ._CH',             # 0E
        'ED6_DT07/CH01180 ._CH',             # 0F
        'ED6_DT07/CH01200 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01170P._CP',             # 02
        'ED6_DT07/CH01130P._CP',             # 03
        'ED6_DT07/CH01470P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01140P._CP',             # 0C
        'ED6_DT07/CH01680P._CP',             # 0D
        'ED6_DT07/CH02440P._CP',             # 0E
        'ED6_DT07/CH01180P._CP',             # 0F
        'ED6_DT07/CH01200P._CP',             # 10
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -20110,
        Z                   = 8000,
        Y                   = 121830,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -42770,
        Z                   = 8000,
        Y                   = 129500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -44640,
        Z                   = -4000,
        Y                   = 151290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -18770,
        Z                   = 8000,
        Y                   = 89560,
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


    DeclActor(
        TriggerX            = -19980,
        TriggerZ            = 8000,
        TriggerY            = 119710,
        TriggerRange        = 400,
        ActorX              = -20110,
        ActorZ              = 9500,
        ActorY              = 121830,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41010,
        TriggerZ            = 8000,
        TriggerY            = 122500,
        TriggerRange        = 800,
        ActorX              = -41010,
        ActorZ              = 10200,
        ActorY              = 122500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38900,
        TriggerZ            = 8400,
        TriggerY            = 122040,
        TriggerRange        = 800,
        ActorX              = -38900,
        ActorZ              = 9900,
        ActorY              = 122040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37E",          # 00, 0
        "Function_1_3B0",          # 01, 1
        "Function_2_3E8",          # 02, 2
        "Function_3_555",          # 03, 3
        "Function_4_55A",          # 04, 4
        "Function_5_804",          # 05, 5
        "Function_6_D42",          # 06, 6
        "Function_7_E53",          # 07, 7
        "Function_8_134C",         # 08, 8
        "Function_9_144B",         # 09, 9
        "Function_10_14A3",        # 0A, 10
        "Function_11_14DD",        # 0B, 11
        "Function_12_159C",        # 0C, 12
    )


    def Function_0_37E(): pass

    label("Function_0_37E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38A")

    label("loc_38A")

    OP_A3(0x3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3AF")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_A2(0x3)
    Event(0, 7)

    label("loc_3AF")

    Return()

    # Function_0_37E end

    def Function_1_3B0(): pass

    label("Function_1_3B0")

    OP_16(0x2, 0xFA0, 0xFFFD6020, 0x4E20, 0x230053)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3D8")
    OP_A3(0x3)
    OP_B1("T3102_1")
    Jump("loc_3E7")

    label("loc_3D8")

    OP_B1("T3102_2")
    OP_71(0x400, 0x0)
    ExitThread()

    label("loc_3E7")

    Return()

    # Function_1_3B0 end

    def Function_2_3E8(): pass

    label("Function_2_3E8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_53F")

    label("loc_40D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_426")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_53F")

    label("loc_426")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_53F")

    label("loc_43F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_458")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_53F")

    label("loc_458")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_471")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_53F")

    label("loc_471")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_53F")

    label("loc_48A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A3")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_53F")

    label("loc_4A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BC")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_53F")

    label("loc_4BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_53F")

    label("loc_4DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_53F")

    label("loc_4F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_510")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_53F")

    label("loc_510")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_53F")

    label("loc_529")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_53F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_554")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_53F")

    label("loc_554")

    Return()

    # Function_2_3E8 end

    def Function_3_555(): pass

    label("Function_3_555")

    Call(0, 4)
    Return()

    # Function_3_555 end

    def Function_4_55A(): pass

    label("Function_4_55A")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 3)), scpexpr(EXPR_END)), "loc_71A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_641")

    ChrTalk(    #0
        0x18,
        (
            "You do my job long enough, you start being able\x01",
            "to work out whether people are using the ships\x01",
            "for work or personal business reeeal quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x18,
        (
            "It just happens, you know? So don't get too mad,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_717")

    label("loc_641")


    ChrTalk(    #2
        0x18,
        "Sorry for teasing you like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x18,
        "I'll be honest, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x18,
        (
            "You do my job long enough, you start being able\x01",
            "to work out whether people are using the ships\x01",
            "for work or personal business reeeal quick.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_717")

    Jump("loc_800")

    label("loc_71A")


    ChrTalk(    #5
        0x18,
        "What's goin' on, Agate? Figured you'd swing by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x18,
        "Don't think I don't know why you're here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x18,
        "Last Friday of the month's always busy, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x106,
        "#057F*glare*\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #9
        0x18,
        "H-Heeey... No need for that look...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F8B)

    label("loc_800")

    TalkEnd(0x18)
    Return()

    # Function_4_55A end

    def Function_5_804(): pass

    label("Function_5_804")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 5)), scpexpr(EXPR_END)), "loc_A02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8ED")

    ChrTalk(    #10
        0x19,
        (
            "#691FI'd love to take Dan along on the salvage\x01",
            "operation with me.\x02\x03",

            "The guy's up to his eyeballs in his own work,\x01",
            "though, and I ain't got the time to see him,\x01",
            "anyway. Ahh, well.\x02\x03",

            "Maybe some other time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FF")

    label("loc_8ED")


    ChrTalk(    #11
        0x19,
        (
            "#690FCome to think of it, I heard Dan and Erika're\x01",
            "back in town now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x106,
        (
            "#552F(Erika?)\x02\x03",

            "(He's gotta mean shortstuff's mom, right?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x19,
        (
            "#691FShame I really haven't got time to drop by and\x01",
            "see 'em today.\x02\x03",

            "Maybe they'd be up for drinks if we're all free\x01",
            "another day.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9FF")

    Jump("loc_D3E")

    label("loc_A02")


    ChrTalk(    #14
        0x19,
        "#691FYo, Agate! Long time no see, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x106,
        (
            "#052FHuh. I wasn't expecting to run into you here.\x02\x03",

            "#051FI heard you were busy as hell lately going around\x01",
            "everywhere and gettin' Liberl's orbal facilities up\x01",
            "and running again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x19,
        (
            "#691FHaha. I sure was.\x02\x03",

            "#690FThen after that, I had to hole myself up in\x01",
            "Leiston Fortress and buckle down on the\x01",
            "necessary repairs to the Arseille.\x02\x03",

            "And now THAT's done, so I'm finally back\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        "#555FFor the love of Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x19,
        (
            "#691FHeh. And, oh, it's only gonna get worse from here.\x02\x03",

            "We've got the loading equipment back on board,\x01",
            "so now we can get down to real work: salvaging.\x02\x03",

            "Trying to pull the Liber Ark out of the lake has\x01",
            "been on the cards for a while now, but now we\x01",
            "can finally get started on it.\x02\x03",

            "Just been too busy to get started on it any earlier,\x01",
            "much as we wanted to.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_A2(0x2F8D)

    label("loc_D3E")

    TalkEnd(0xFE)
    Return()

    # Function_5_804 end

    def Function_6_D42(): pass

    label("Function_6_D42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_E4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_DF1")

    ChrTalk(    #19
        0xFE,
        "We're off to Valleria Lake next, apparently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I've heard we're going to be doing some kind\x01",
            "of investigation there...but an investigation of\x01",
            "what?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4F")

    label("loc_DF1")


    ChrTalk(    #21
        0xFE,
        "We're gonna be leaving port in 15 minutes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "*sigh* This ship sure is busy lately.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_E4F")

    TalkEnd(0xFE)
    Return()

    # Function_6_D42 end

    def Function_7_E53(): pass

    label("Function_7_E53")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    ClearMapFlags(0x1)
    ClearMapFlags(0x10)
    OP_6D(-32960, -4000, 149340, 0)
    OP_67(0, 10520, -10000, 0)
    OP_6B(10800, 0)
    OP_6C(70000, 0)
    OP_6E(175, 0)
    SetChrFlags(0x19, 0x80)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_A1(0x1B, 0x4)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()
    SetChrPos(0x1B, -34000, -150, 148000, 0)
    SetChrFlags(0x1B, 0x4)
    OP_A1(0x1C, 0x5)
    OP_72(0x405, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x1C, -34000, -10150, 148000, 0)
    SetChrFlags(0x1C, 0x4)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x406, 0x0)
    ExitThread()
    OP_6F(0x3, 100)
    OP_6F(0x4, 60)
    OP_6F(0x5, 0)
    FadeToBright(1500, 0)
    OP_C8(0x200, 0x46, "C_PLAC08._CH", 0x0, 0x7D0)

    def lambda_F49():
        OP_6D(-32960, -6000, 149340, 11000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_F49)

    def lambda_F61():
        OP_6C(50000, 11000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_F61)

    def lambda_F71():
        OP_67(0, 6880, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_F71)

    def lambda_F89():
        OP_6B(7800, 11000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_F89)
    Call(0, 8)
    OP_43(0x16, 0x3, 0x0, 0x9)
    Sleep(1200)
    OP_43(0x15, 0x3, 0x0, 0x9)
    Sleep(900)
    OP_43(0x10, 0x3, 0x0, 0x9)
    Sleep(1400)
    OP_43(0x17, 0x3, 0x0, 0x9)
    Sleep(2000)
    OP_43(0x106, 0x3, 0x0, 0xA)
    Sleep(6000)
    Fade(1000)
    OP_6D(-47600, -4000, 144600, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x106, 0x3)
    Sleep(300)

    ChrTalk(    #23
        0x106,
        (
            "#551FBah... Can't believe I'm going through with\x01",
            "this.\x02\x03",

            "I should never've given in to pressure and\x01",
            "promised to come here once a month in the\x01",
            "first place.\x02\x03",

            "#552FHavin' to adjust my schedule all the time just\x01",
            "so I can come all this way to eat is such a pain\x01",
            "in the ass...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x106)
    Sleep(300)
    OP_8C(0x106, 180, 400)
    Sleep(300)

    ChrTalk(    #24
        0x106,
        "#556F#11P...But, well, whatever. I do owe her, I guess.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_11AA():
        OP_6D(-47600, -4000, 142500, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_11AA)

    def lambda_11C2():
        OP_8E(0xFE, 0xFFFF4A5C, 0xFFFFF060, 0x22858, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_11C2)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x106, 0x1)

    def lambda_11E7():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_11E7)
    Sleep(1000)
    OP_62(0x106, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #25
        0x106,
        (
            "#055F#11PWh-What the hell? I just felt this horrible chill\x01",
            "run down my spine... What was that for?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_128A():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_128A)
    Sleep(1500)

    ChrTalk(    #26
        0x106,
        (
            "#555F#11P???\x02\x03",

            "Okay, then...\x02\x03",

            "#552FDoesn't seem like I've caught a cold or anything...\x01",
            "Probably no big deal.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_131A():
        OP_8E(0xFE, 0xFFFF4A5C, 0x0, 0x1EE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_131A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_E53 end

    def Function_8_134C(): pass

    label("Function_8_134C")


    def lambda_1352():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1352)

    def lambda_136D():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFE412, 0x24220, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_136D)
    WaitChrThread(0x1B, 0x1)

    def lambda_138D():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD85A, 0x24220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_138D)
    WaitChrThread(0x1B, 0x1)

    def lambda_13AD():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_13AD)
    WaitChrThread(0x1B, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x1B, -34000, -11150, 148000, 0)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    Sleep(2500)
    OP_6F(0x4, 410)
    OP_70(0x4, 0x1CC)
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x4)
    OP_44(0x0, 0x1)
    Return()

    # Function_8_134C end

    def Function_9_144B(): pass

    label("Function_9_144B")

    SetChrPos(0xFE, -33850, -4000, 149000, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF7BC6, 0xFFFFF060, 0x2321C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4A5C, 0xFFFFF060, 0x2321C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4A5C, 0x0, 0x1EE88, 0x7D0, 0x0)
    Return()

    # Function_9_144B end

    def Function_10_14A3(): pass

    label("Function_10_14A3")

    SetChrPos(0xFE, -33850, -4000, 149000, 180)
    OP_8E(0xFE, 0xFFFF7BC6, 0xFFFFF060, 0x2321C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4A5C, 0xFFFFF060, 0x2321C, 0x7D0, 0x0)
    Return()

    # Function_10_14A3 end

    def Function_11_14DD(): pass

    label("Function_11_14DD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #27
        (
            "\x07\x05Airship Arrivals & Departures\x01\x09\x09",
            "⇒ To Grancel\x01\x09\x09",
            "⇒ To Ruan\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #28
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_14DD end

    def Function_12_159C(): pass

    label("Function_12_159C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #29
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_159C end

    SaveToFile()

Try(main)
