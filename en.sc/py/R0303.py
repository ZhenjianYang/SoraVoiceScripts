from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0303   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0303.x',
        MapIndex            = 21,
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
        'Thunder Quake',                        # 9
        'Private Heinz',                        # 10
        'Miner Landan',                         # 11
        'Agate',                                # 12
        'Targeting Camera',                     # 13
        'Malga Trail',                          # 14
        'Malga Trail',                          # 15
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01500 ._CH',             # 01
        'ED6_DT06/CH20053 ._CH',             # 02
        'ED6_DT09/CH10900 ._CH',             # 03
        'ED6_DT09/CH10901 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01500P._CP',             # 01
        'ED6_DT06/CH20053P._CP',             # 02
        'ED6_DT09/CH10900P._CP',             # 03
        'ED6_DT09/CH10901P._CP',             # 04
    )

    DeclNpc(
        X                   = -420,
        Z                   = -20,
        Y                   = -34790,
        Direction           = 180,
        Unknown2            = 3,
        Unknown3            = 196608,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -166100,
        Z                   = 100,
        Y                   = 127500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -166100,
        Z                   = 100,
        Y                   = 127500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        X                   = -167010,
        Z                   = -70,
        Y                   = 78790,
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
        X                   = -2070,
        Z                   = -120,
        Y                   = -72730,
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
        X                   = -4700,
        Y                   = -2000,
        Z                   = -62600,
        Range               = 1200,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF1668,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -15720,
        Y                   = -2000,
        Z                   = -24750,
        Range               = 13360,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFFB08C,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -2500,
        Y                   = -6100,
        Z                   = -8670,
        Range               = 2500,
        Unknown_10          = 0x2710,
        Unknown_14          = 0xFFFFF254,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -168250,
        Y                   = -1000,
        Z                   = 128800,
        Range               = -164500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1F2E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -420,
        Y                   = -1000,
        Z                   = -34790,
        Range               = 2000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = -13840,
        TriggerZ            = -130,
        TriggerY            = -13720,
        TriggerRange        = 1000,
        ActorX              = -13620,
        ActorZ              = -140,
        ActorY              = -12960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_276",          # 00, 0
        "Function_1_3C6",          # 01, 1
        "Function_2_59D",          # 02, 2
        "Function_3_5B3",          # 03, 3
        "Function_4_5BE",          # 04, 4
        "Function_5_BEE",          # 05, 5
        "Function_6_BF9",          # 06, 6
        "Function_7_D90",          # 07, 7
        "Function_8_F5F",          # 08, 8
        "Function_9_10EA",         # 09, 9
        "Function_10_1807",        # 0A, 10
        "Function_11_18DB",        # 0B, 11
        "Function_12_1970",        # 0C, 12
        "Function_13_1F92",        # 0D, 13
        "Function_14_207D",        # 0E, 14
        "Function_15_2103",        # 0F, 15
        "Function_16_2192",        # 10, 16
        "Function_17_2275",        # 11, 17
        "Function_18_22FA",        # 12, 18
        "Function_19_237F",        # 13, 19
        "Function_20_2404",        # 14, 20
        "Function_21_2489",        # 15, 21
        "Function_22_2615",        # 16, 22
        "Function_23_267B",        # 17, 23
        "Function_24_26E1",        # 18, 24
        "Function_25_2747",        # 19, 25
    )


    def Function_0_276(): pass

    label("Function_0_276")

    OP_A3(0x1970)
    OP_A3(0x1971)
    OP_A3(0x1972)
    OP_A3(0x1973)
    OP_A3(0x1974)
    OP_A3(0x1975)
    OP_A3(0x1976)
    OP_A3(0x1977)
    OP_A3(0x1978)
    OP_A3(0x1979)
    OP_A3(0x197A)
    OP_A3(0x197B)
    OP_A3(0x197C)
    OP_A3(0x1FC0)
    OP_A3(0x1FC1)
    OP_A3(0x1FC2)
    OP_A3(0x1FC3)
    OP_A3(0x1FC4)
    OP_A3(0x1FC5)
    OP_A3(0x1FC6)
    OP_A3(0x1FC7)
    OP_A3(0x1FC8)
    OP_A3(0x1FC9)
    OP_A3(0x1FCA)
    OP_A3(0x1FCB)
    OP_A3(0x1FCC)
    OP_A3(0x1FCD)
    OP_A3(0x1FCE)
    OP_A3(0x1FCF)
    OP_A3(0x1FD0)
    OP_A3(0x1FD1)
    OP_A3(0x1FD2)
    OP_A3(0x1FD3)
    OP_A3(0x1FD4)
    OP_A3(0x1FD5)
    OP_A3(0x1FD6)
    OP_A3(0x1FD7)
    OP_A3(0x1FD8)
    OP_A3(0x1FD9)
    OP_A3(0x1FDA)
    OP_A3(0x1FDB)
    OP_A3(0x1FDC)
    OP_A3(0x1FDD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_319")
    SetChrPos(0x9, -2440, 30, -23500, 180)
    ClearChrFlags(0x9, 0x80)

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330")
    SetChrFlags(0xA, 0x80)
    Jump("loc_346")

    label("loc_330")

    SetChrPos(0xA, -168160, -10, 126410, 90)
    ClearChrFlags(0xA, 0x80)

    label("loc_346")

    Jump("loc_389")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_353")
    Jump("loc_389")

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_362")
    SetChrFlags(0xA, 0x80)
    Jump("loc_389")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_382")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -163860, 40, 125420, 315)
    Jump("loc_389")

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_389")

    label("loc_389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_39F")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_3C5")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3B5")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_3C5")

    label("loc_3B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5")
    Event(0, 21)

    label("loc_3C5")

    Return()

    # Function_0_276 end

    def Function_1_3C6(): pass

    label("Function_1_3C6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3E6"),
        (101, "loc_3E6"),
        (105, "loc_3E6"),
        (102, "loc_412"),
        (103, "loc_412"),
        (104, "loc_412"),
        (SWITCH_DEFAULT, "loc_43E"),
    )


    label("loc_3E6")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFD7790, 0x230011)
    ClearChrFlags(0xD, 0x4)
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x2F8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43E")

    label("loc_412")

    OP_16(0x2, 0xFA0, 0xFFFB8390, 0xFFFFBD98, 0x23006A)
    ClearChrFlags(0xE, 0x4)
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x31A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x81), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43E")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_458")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_468")
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x1)
    Jump("loc_46E")

    label("loc_468")

    OP_10(0x3, 0x1)
    OP_10(0x4, 0x0)

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48C")
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x4, 0x80)
    Jump("loc_49E")

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x4, 0x80)

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x326, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0")
    OP_6F(0x0, 0)
    Jump("loc_4B7")

    label("loc_4B0")

    OP_6F(0x0, 60)

    label("loc_4B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_512")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4E8")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)
    Jump("loc_512")

    label("loc_4E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_512")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_512")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_521")
    Jump("loc_571")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_571")
    LoadEffect(0x0, "map\\\\mp086_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 6000, -8130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_57D")
    OP_B2(0x0, 0x3, 0x80)

    label("loc_57D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_596")
    OP_10(0x1, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_59C")

    label("loc_596")

    OP_10(0x1, 0x1)
    OP_10(0x5, 0x0)

    label("loc_59C")

    Return()

    # Function_1_3C6 end

    def Function_2_59D(): pass

    label("Function_2_59D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_59D")

    label("loc_5B2")

    Return()

    # Function_2_59D end

    def Function_3_5B3(): pass

    label("Function_3_5B3")

    TalkBegin(0xA)
    Call(0, 4)
    TalkEnd(0xA)
    Return()

    # Function_3_5B3 end

    def Function_4_5BE(): pass

    label("Function_4_5BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_6D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_671")

    ChrTalk(    #0
        0xA,
        (
            "Hey! Ladies, thanks for your help\x01",
            "during that accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        (
            "The other miners are already back\x01",
            "to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xA,
        (
            "You're welcome to go say hello\x01",
            "if you like.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6D5")

    label("loc_671")


    ChrTalk(    #3
        0xA,
        (
            "Thanks for your help during that\x01",
            "accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "If you'd like, come by and say hello\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D5")

    Jump("loc_BED")

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_9C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_738")

    ChrTalk(    #5
        0xA,
        (
            "Sorry, can't let you in. We're starting\x01",
            "work again as of today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E7")

    label("loc_738")


    ChrTalk(    #6
        0xA,
        "Hey, bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        "The boss is finally coming back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "That means we'll be able to return\x01",
            "to work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "So, uh, sorry, but we can't let any\x01",
            "non-miners in right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7E7")

    Jump("loc_9C4")

    label("loc_7EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_864")

    ChrTalk(    #10
        0xA,
        "We're starting work up again today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "So, uh, sorry, but the mine's off limits\x01",
            "to non-miners right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C4")

    label("loc_864")


    ChrTalk(    #12
        0xA,
        (
            "Hey, guys. Thanks again for everything\x01",
            "you've done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "We're gettin' ready to go back to work,\x01",
            "but the boss is missing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        (
            "The rest of the miners are done with\x01",
            "preparations and are on standby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        (
            "I think there's some kinda trouble at\x01",
            "Chief Gaton's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "I don't know the details, but I sure wish\x01",
            "he'd come back to the mine already.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9C4")

    Jump("loc_BED")

    label("loc_9C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_AF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A5D")

    ChrTalk(    #17
        0xA,
        (
            "Right now, your bracer buddies are\x01",
            "inside getting everyone evacuated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "You've saved our hides! Now we can\x01",
            "get back to town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF5")

    label("loc_A5D")


    ChrTalk(    #19
        0xA,
        "Hey, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xA,
        (
            "Right now, your bracer buddies are\x01",
            "inside getting everyone evacuated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "You've saved our hides! Now we can\x01",
            "get back to town.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_AF5")

    Jump("loc_BED")

    label("loc_AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_BED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B51")

    ChrTalk(    #22
        0xA,
        (
            "Sorry, but you know the mine's off limits.\x01",
            "Gotta ask you to leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BED")

    label("loc_B51")


    ChrTalk(    #23
        0xA,
        (
            "Hey, you're those bracers from way back,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        (
            "Sorry, but the mine's off limits to\x01",
            "non-miners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        "Sorry, but I'll have to ask you to leave.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BED")

    Return()

    # Function_4_5BE end

    def Function_5_BEE(): pass

    label("Function_5_BEE")

    TalkBegin(0xB)
    Call(0, 6)
    TalkEnd(0xB)
    Return()

    # Function_5_BEE end

    def Function_6_BF9(): pass

    label("Function_6_BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_D8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C5B")

    ChrTalk(    #26
        0xB,
        (
            "#050FOlivier and Zin are rounding up\x01",
            "the miners.\x02\x03",

            "You guys get to the farm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8F")

    label("loc_C5B")


    ChrTalk(    #27
        0xB,
        (
            "#052FHuh? Estelle? Scherazard?\x02\x03",

            "What're you doin' here? Weren't you\x01",
            "headin' for the farm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1008FUm, we were...just on our way?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #29
        0xB,
        (
            "#057FWe split into two groups for a reason.\x02\x03",

            "Those people need help. They're your\x01",
            "friends, right? Hurry up and get to that\x01",
            "farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1007FU-Understood...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D8F")

    Return()

    # Function_6_BF9 end

    def Function_7_D90(): pass

    label("Function_7_D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31F, 6)), scpexpr(EXPR_END)), "loc_D98")
    Return()

    label("loc_D98")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Exterminate\x01",      # 0
            "Leave Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_E8C"),
        (SWITCH_DEFAULT, "loc_EAF"),
    )


    label("loc_E8C")

    Fade(500)
    OP_89(0x0, -580, -40, -40880, 357)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_EAF")

    Battle(0xEEC, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -580, -40, -40880, 357)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_EE8"),
        (1, "loc_EEB"),
        (SWITCH_DEFAULT, "loc_EEE"),
    )


    label("loc_EE8")

    EventEnd(0x0)
    Return()

    label("loc_EEB")

    OP_B4(0x0)
    Return()

    label("loc_EEE")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x4, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05Exterminated monster!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x18FE)
    OP_28(0xB0, 0x4, 0x10)
    OP_28(0xB0, 0x4, 0x2)
    OP_28(0xB0, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_7_D90 end

    def Function_8_F5F(): pass

    label("Function_8_F5F")

    OP_EA(0x2, 0xCA, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x326, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1037")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_FD0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1933)
    Jump("loc_1034")

    label("loc_FD0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_1034")

    Jump("loc_10DC")

    label("loc_1037")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "\x07\x05As you open the treasure chest, you realize that\x01",
            "coming back for more is probably selfish.\x01",
            "You decide to leave what remains to others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_10DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_F5F end

    def Function_9_10EA(): pass

    label("Function_9_10EA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1101")
    Call(0, 14)
    Call(0, 15)

    label("loc_1101")

    OP_6D(-1710, -30, -25410, 0)
    OP_67(0, 10030, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(315000, 0)
    OP_6E(393, 0)
    SetChrPos(0x101, 1330, -30, -53480, 0)
    SetChrPos(0x102, 140, -20, -53920, 0)
    SetChrPos(0xF8, 1340, -40, -55460, 0)
    SetChrPos(0xF9, -110, -30, -55920, 0)

    def lambda_1188():
        OP_8E(0xFE, 0x532, 0xFFFFFFE2, 0xFFFF54FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1188)

    def lambda_11A3():
        OP_8E(0xFE, 0x8C, 0xFFFFFFEC, 0xFFFF5538, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11A3)

    def lambda_11BE():
        OP_8E(0xFE, 0x53C, 0xFFFFFFD8, 0xFFFF4FFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_11BE)

    def lambda_11D9():
        OP_8E(0xFE, 0xFFFFFF92, 0xFFFFFFE2, 0xFFFF5024, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_11D9)

    def lambda_11F4():
        OP_6D(120, -40, -43020, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11F4)
    OP_C8(0x200, 0x46, "C_PLAC19._CH", 0x1, 0x3E8)
    OP_DE("Esmelas Tower")
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(250, -20, -43960, 0)
    OP_67(0, 9530, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #36
        0x101,
        (
            "#1002F#6PRight, time to take care of things.\x02\x03",

            "We should get to the top\x01",
            "of the tower, pronto.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#1043F#6PYes. Something seems...\x01",
            "wrong, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1004F#6PDoes it?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 850, -30, -32460, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)

    NpcTalk(    #39
        0x9,
        "Man's Voice",
        "#3PIt's you guys...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C0")
    OP_62(0xF8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_13F4")

    label("loc_13C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E2")
    OP_62(0xF8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_13F4")

    label("loc_13E2")

    OP_62(0xF8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_13F4")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141B")
    OP_62(0xF9, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_144F")

    label("loc_141B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143D")
    OP_62(0xF9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_144F")

    label("loc_143D")

    OP_62(0xF9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_144F")

    Sleep(1000)

    def lambda_145A():
        OP_6D(120, -40, -42500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_145A)

    def lambda_1472():
        OP_67(0, 9040, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1472)
    OP_8E(0x9, 0x1F4, 0xFFFFFFC4, 0xFFFF5D12, 0xFA0, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #40
        0x9,
        (
            "#4PAre you the bracers\x01",
            "we were told about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1006F#5PYeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        "#1042F#6PYou're part of the scouting force?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "#4PY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#4PI stayed behind to report the status\x01",
            "of the tower to you guys.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C6")

    ChrTalk(    #45
        0x106,
        (
            "#555F#5PYou got nailed by some\x01",
            "clown in a mask, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_15C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1613")

    ChrTalk(    #46
        0x103,
        (
            "#022F#5PYou were attacked by a\x01",
            "man in a mask, correct?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_1613")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_165B")

    ChrTalk(    #47
        0x108,
        (
            "#072F#5PYou were attacked by a\x01",
            "masked man, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_165B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B3")

    ChrTalk(    #48
        0x109,
        (
            "#1063F#5PSo apparently some schmoe in\x01",
            "a mask roughed you guys up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_16B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F8")

    ChrTalk(    #49
        0x105,
        (
            "#043F#5PA man in an opera mask\x01",
            "attacked you, yes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F8")


    ChrTalk(    #50
        0x9,
        "#4PY-Yeah, but that's not all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "#4PHow the hell do I...?\x01",
            "It's the tower. It's...off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1015F#5PIt's 'off'? How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#4PI can't...\x01",
            "You'll get it when you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        "#4PC'mere, check out the entrance.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 500)
    OP_90(0x9, 0x0, 0x0, 0x3A98, 0xFA0, 0x0)
    SetChrPos(0x9, -2440, 30, -23500, 180)
    OP_4B(0x9, 255)
    OP_A2(0x1E03)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_9_10EA end

    def Function_10_1807(): pass

    label("Function_10_1807")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1819")
    Return()

    label("loc_1819")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05Return to the Arseille?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Return]\x01",            # 0
            "[Don't Return]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BA")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18DA")

    label("loc_18BA")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_18DA")

    Return()

    # Function_10_1807 end

    def Function_11_18DB(): pass

    label("Function_11_18DB")

    EventBegin(0x0)
    OP_6D(-1900, -90, -56520, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1900, -90, -56520, 0)
    SetChrPos(0x102, -1900, -90, -56520, 0)
    SetChrPos(0xF8, -1900, -90, -56520, 0)
    SetChrPos(0xF9, -1900, -90, -56520, 0)
    OP_48()
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_11_18DB end

    def Function_12_1970(): pass

    label("Function_12_1970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_197D")
    Return()

    label("loc_197D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19A2")
    Call(0, 14)
    Call(0, 15)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_19A2")

    Fade(1000)
    OP_6D(-540, 100, -23090, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 800, 40, -22800, 0)
    SetChrPos(0x102, -400, 90, -22800, 0)
    SetChrPos(0xF8, 800, 70, -24200, 0)
    SetChrPos(0xF9, -400, 10, -24200, 0)
    OP_8C(0x9, 0, 0)
    OP_4A(0x9, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #56
        0x101,
        "#1004F#6PWhat the--?!\x02",
    )

    CloseMessageWindow()

    def lambda_1A5A():
        OP_6D(-930, 2000, -16490, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A5A)

    def lambda_1A72():
        OP_67(0, 3110, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A72)

    def lambda_1A8A():
        OP_6B(2730, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A8A)

    def lambda_1A9A():
        OP_6C(349000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A9A)

    def lambda_1AAA():
        OP_6E(567, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1AAA)
    WaitChrThread(0x101, 0x3)
    Fade(1000)
    OP_6D(0, 4890, -15580, 0)
    OP_67(0, 1310, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(0, 0)
    OP_6E(412, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #57
        "\x07\x00#1020FThat's... What?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7D")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #58
        "\x07\x00#065F#5PAn energy field of some kind!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1CC8")

    label("loc_1B7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD3")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("Kloe")

    AnonymousTalk(    #59
        (
            "\x07\x00#042F#5PSome sort of...field?\x01",
            "A barrier? Or...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1CC8")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C28")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #60
        "\x07\x00#1069F#5POh, hell... A barrier of some sort!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1CC8")

    label("loc_1C28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C6E")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #61
        "\x07\x00#072F#5PA barrier, maybe? No...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1CC8")

    label("loc_1C6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC8")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #62
        (
            "\x07\x00#022F#5PIt looks like a barrier\x01",
            "of some sort...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1CC8")

    Sleep(100)
    Fade(1000)
    TurnDirection(0x9, 0x102, 0)
    OP_6D(-1450, 90, -22590, 0)
    OP_67(0, 7770, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(283, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #63
        0x9,
        "#6PIt was like this when we arrived.\x02",
    )

    CloseMessageWindow()

    def lambda_1D4C():

        label("loc_1D4C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1D4C")

    QueueWorkItem2(0x101, 1, lambda_1D4C)
    Sleep(50)

    def lambda_1D62():

        label("loc_1D62")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1D62")

    QueueWorkItem2(0x102, 1, lambda_1D62)
    Sleep(50)

    def lambda_1D78():

        label("loc_1D78")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1D78")

    QueueWorkItem2(0xF8, 1, lambda_1D78)
    Sleep(50)

    def lambda_1D8E():

        label("loc_1D8E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1D8E")

    QueueWorkItem2(0xF9, 1, lambda_1D8E)

    ChrTalk(    #64
        0x9,
        (
            "#6PWhen we tried to investigate,\x01",
            "that guy in the mask showed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1043F#4P...\x02\x03",

            "#1042FIs the barrier blocking entry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "#6PThe guy in the mask went\x01",
            "in, so it's probably okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#6PI thought about giving chase,\x01",
            "but my entire team's out of action!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1007F#2PMan...\x02\x03",

            "#1002FOkay, leave this to us and\x01",
            "get back to your squad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "#6PUnderstood.\x01",
            "May Aidios guide your steps!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 500)

    def lambda_1F2A():
        OP_6D(-690, 20, -27800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F2A)
    OP_8E(0x9, 0xFFFFFF42, 0xFFFFFFF6, 0xFFFF6348, 0x1388, 0x0)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0x101, 0x0)

    def lambda_1F60():
        OP_6D(-1450, 90, -22590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F60)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_A2(0x1E04)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_12_1970 end

    def Function_13_1F92(): pass

    label("Function_13_1F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F9F")
    Return()

    label("loc_1F9F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2024")
    TurnDirection(0xB, 0x0, 400)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    OP_4A(0xB, 255)
    SetChrFlags(0xB, 0x40)
    Call(0, 6)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x1EC30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_92(0x0, 0xC, 0x0, 0xBB8, 0x0)
    OP_8C(0xB, 0, 0)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0xB, 255)
    ClearChrFlags(0xB, 0x40)
    Jump("loc_207C")

    label("loc_2024")

    TurnDirection(0xA, 0x0, 400)
    OP_4A(0xA, 255)
    SetChrFlags(0xA, 0x40)
    Call(0, 4)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x1EC30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_92(0x0, 0xC, 0x0, 0xBB8, 0x0)
    OP_8C(0xA, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0xA, 255)
    ClearChrFlags(0xA, 0x40)

    label("loc_207C")

    Return()

    # Function_13_1F92 end

    def Function_14_207D(): pass

    label("Function_14_207D")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20F6"),
        (1, "loc_20FC"),
        (SWITCH_DEFAULT, "loc_2102"),
    )


    label("loc_20F6")

    OP_A2(0x1200)
    Jump("loc_2102")

    label("loc_20FC")

    OP_A2(0x1201)
    Jump("loc_2102")

    label("loc_2102")

    Return()

    # Function_14_207D end

    def Function_15_2103(): pass

    label("Function_15_2103")

    FadeToDark(0, 0, -1)
    OP_6D(55450, 4000, 13070, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_15_2103 end

    def Function_16_2192(): pass

    label("Function_16_2192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2274")
    EventBegin(0x0)
    Fade(500)
    ClearMapFlags(0x1)
    OP_6D(-40, 4000, -8710, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x101, 850, 4000, -10070, 0)
    SetChrPos(0x102, -360, 4000, -10110, 0)
    SetChrPos(0xF8, 820, 3600, -11500, 0)
    SetChrPos(0xF9, -450, 3600, -11500, 0)
    OP_43(0x101, 0x0, 0x0, 0x11)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0x12)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0x13)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0x14)
    WaitChrThread(0x3, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/C0700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2274")

    Return()

    # Function_16_2192 end

    def Function_17_2275(): pass

    label("Function_17_2275")

    OP_91(0xFE, 0x0, 0x0, 0x708, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_22BA():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22BA)

    def lambda_22D4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22D4)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_17_2275 end

    def Function_18_22FA(): pass

    label("Function_18_22FA")

    OP_91(0xFE, 0x0, 0x0, 0x708, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_233F():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_233F)

    def lambda_2359():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2359)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_18_22FA end

    def Function_19_237F(): pass

    label("Function_19_237F")

    OP_91(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_23C4():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23C4)

    def lambda_23DE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23DE)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_19_237F end

    def Function_20_2404(): pass

    label("Function_20_2404")

    OP_91(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_2449():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2449)

    def lambda_2463():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2463)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_20_2404 end

    def Function_21_2489(): pass

    label("Function_21_2489")

    EventBegin(0x0)
    OP_6D(-40, 4000, -8710, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x101, 500, 4400, -7000, 180)
    SetChrPos(0x102, -500, 4400, -7000, 180)
    SetChrPos(0xF8, 500, 4400, -7000, 180)
    SetChrPos(0xF9, -500, 4400, -7000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0x16)
    Sleep(800)
    OP_43(0x102, 0x0, 0x0, 0x17)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x19)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(100, 4000, -10180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 100, 4000, -10180, 180)
    SetChrPos(0x1, 100, 4000, -10180, 180)
    SetChrPos(0x2, 100, 4000, -10180, 180)
    SetChrPos(0x3, 100, 4000, -10180, 180)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_21_2489 end

    def Function_22_2615(): pass

    label("Function_22_2615")

    OP_22(0x99, 0x0, 0x64)

    def lambda_2620():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2620)

    def lambda_263A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_263A)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_265B():
        OP_8F(0xFE, 0x1F4, 0xFA0, 0xFFFFD2CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_265B)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_22_2615 end

    def Function_23_267B(): pass

    label("Function_23_267B")

    OP_22(0x99, 0x0, 0x64)

    def lambda_2686():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2686)

    def lambda_26A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26A0)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_26C1():
        OP_8F(0xFE, 0xFFFFFE0C, 0xFA0, 0xFFFFD2CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26C1)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_23_267B end

    def Function_24_26E1(): pass

    label("Function_24_26E1")

    OP_22(0x99, 0x0, 0x64)

    def lambda_26EC():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26EC)

    def lambda_2706():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2706)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_2727():
        OP_8F(0xFE, 0x1F4, 0xE10, 0xFFFFD698, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2727)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_24_26E1 end

    def Function_25_2747(): pass

    label("Function_25_2747")

    OP_22(0x99, 0x0, 0x64)

    def lambda_2752():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2752)

    def lambda_276C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_276C)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_278D():
        OP_8F(0xFE, 0xFFFFFE0C, 0xE10, 0xFFFFD698, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_278D)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_25_2747 end

    SaveToFile()

Try(main)
