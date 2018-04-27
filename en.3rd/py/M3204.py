from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M3204   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3204.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        'Brig. General Bright',                 # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT27/CH04670 ._CH',             # 01
        'ED6_DT27/CH04679 ._CH',             # 02
        'ED6_DT26/CH20307 ._CH',             # 03
        'ED6_DT26/CH20715 ._CH',             # 04
        'ED6_DT07/CH00330 ._CH',             # 05
        'ED6_DT07/CH00331 ._CH',             # 06
        'ED6_DT07/CH00430 ._CH',             # 07
        'ED6_DT07/CH00431 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT27/CH04670P._CP',             # 01
        'ED6_DT27/CH04679P._CP',             # 02
        'ED6_DT26/CH20307P._CP',             # 03
        'ED6_DT26/CH20715P._CP',             # 04
        'ED6_DT07/CH00330P._CP',             # 05
        'ED6_DT07/CH00331P._CP',             # 06
        'ED6_DT07/CH00430P._CP',             # 07
        'ED6_DT07/CH00431P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -63160,
        Z                   = 0,
        Y                   = 88730,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20280,
        Z                   = 0,
        Y                   = 50020,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 900,
        Z                   = 0,
        Y                   = 24970,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15950,
        Z                   = 0,
        Y                   = -68010,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 61880,
        TriggerZ            = 0,
        TriggerY            = 26870,
        TriggerRange        = 1000,
        ActorX              = 61880,
        ActorZ              = 2000,
        ActorY              = 26870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15240,
        TriggerZ            = 1000,
        TriggerY            = -34250,
        TriggerRange        = 1000,
        ActorX              = -15240,
        ActorZ              = 1000,
        ActorY              = -34250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53910,
        TriggerZ            = 1000,
        TriggerY            = -68930,
        TriggerRange        = 1000,
        ActorX              = 53910,
        ActorZ              = 1000,
        ActorY              = -68930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2800,
        TriggerZ            = 1000,
        TriggerY            = 25020,
        TriggerRange        = 1000,
        ActorX              = 2800,
        ActorZ              = 1000,
        ActorY              = 25020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_24D",          # 01, 1
        "Function_2_2AA",          # 02, 2
        "Function_3_3DF",          # 03, 3
        "Function_4_535",          # 04, 4
        "Function_5_677",          # 05, 5
        "Function_6_680",          # 06, 6
        "Function_7_3366",         # 07, 7
        "Function_8_45C6",         # 08, 8
        "Function_9_4685",         # 09, 9
        "Function_10_475E",        # 0A, 10
        "Function_11_4E2A",        # 0B, 11
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22E")
    Event(0, 5)

    label("loc_22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24C")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_24C")

    Return()

    # Function_0_212 end

    def Function_1_24D(): pass

    label("Function_1_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270")
    OP_6F(0x33, 0)
    Jump("loc_277")

    label("loc_270")

    OP_6F(0x33, 60)

    label("loc_277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289")
    OP_6F(0x34, 0)
    Jump("loc_290")

    label("loc_289")

    OP_6F(0x34, 60)

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2")
    OP_6F(0x35, 0)
    Jump("loc_2A9")

    label("loc_2A2")

    OP_6F(0x35, 60)

    label("loc_2A9")

    Return()

    # Function_1_24D end

    def Function_2_2AA(): pass

    label("Function_2_2AA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_383")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x33, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_318")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x05\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B98)
    Jump("loc_380")

    label("loc_318")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x05\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x05\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x33, 60)
    OP_70(0x33, 0x0)

    label("loc_380")

    Jump("loc_3D1")

    label("loc_383")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05If only I'd come with an explosive trap...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x2E, 0x0)

    label("loc_3D1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2AA end

    def Function_3_3DF(): pass

    label("Function_3_3DF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x34, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A7, 1)"), scpexpr(EXPR_END)), "loc_44D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xA7\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B99)
    Jump("loc_4B5")

    label("loc_44D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xA7\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xA7\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x34, 60)
    OP_70(0x34, 0x0)

    label("loc_4B5")

    Jump("loc_527")

    label("loc_4B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05I hope you at least made sure to not leave fingerprints on the crime scene.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x2F, 0x0)

    label("loc_527")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3DF end

    def Function_4_535(): pass

    label("Function_4_535")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x35, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_5A3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B9A)
    Jump("loc_60B")

    label("loc_5A3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x35, 60)
    OP_70(0x35, 0x0)

    label("loc_60B")

    Jump("loc_669")

    label("loc_60E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05You find a torn note that says: 'chest No. 53 wuz here'\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x30, 0x0)

    label("loc_669")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_535 end

    def Function_5_677(): pass

    label("Function_5_677")

    Call(0, 6)
    Call(0, 7)
    Return()

    # Function_5_677 end

    def Function_6_680(): pass

    label("Function_6_680")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    OP_E0(238, 0x49, 0x2)
    OP_E0(238, 0x4A, 0x3)
    OP_E0(239, 0x4B, 0x2)
    OP_E0(239, 0x4C, 0x3)
    OP_E0(240, 0x4D, 0x2)
    OP_E0(240, 0x4E, 0x3)
    OP_E0(241, 0x4F, 0x2)
    OP_E0(241, 0x50, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 58980, 0, 73020, 180)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x109, 58240, 0, 60860, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_760")
    SetChrPos(0xEF, 59750, 0, 60760, 0)
    SetChrPos(0xF0, 57750, 0, 58900, 0)
    SetChrPos(0xF1, 59800, 0, 59090, 0)
    Jump("loc_7E5")

    label("loc_760")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A4")
    SetChrPos(0xF0, 59750, 0, 60760, 0)
    SetChrPos(0xEF, 57750, 0, 58900, 0)
    SetChrPos(0xF1, 59800, 0, 59090, 0)
    Jump("loc_7E5")

    label("loc_7A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E5")
    SetChrPos(0xF1, 59750, 0, 60760, 0)
    SetChrPos(0xEF, 57750, 0, 58900, 0)
    SetChrPos(0xF0, 59800, 0, 59090, 0)

    label("loc_7E5")

    OP_6D(60100, 0, 61450, 0)
    OP_67(0, 5590, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(45000, 0)
    OP_6E(302, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #9
        0x10,
        "Man's Voice",
        "#4PYou made it, I see.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89D")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_904")

    label("loc_89D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C5")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_904")

    label("loc_8C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_904")

    label("loc_8ED")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_904")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_931")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_998")

    label("loc_931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_959")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_998")

    label("loc_959")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_981")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_998")

    label("loc_981")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_998")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C5")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A2C")

    label("loc_9C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ED")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A2C")

    label("loc_9ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A15")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A2C")

    label("loc_A15")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A2C")

    Sleep(1000)

    def lambda_A37():
        OP_6D(60220, 0, 74050, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_A37)

    def lambda_A4F():
        OP_67(0, 4660, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_A4F)

    def lambda_A67():
        OP_6B(2550, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_A67)

    def lambda_A77():
        OP_6E(285, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_A77)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #10
        0x10C,
        "#112F#1PBrigadier General...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACB")

    ChrTalk(    #11
        0x101,
        "#1025F#1PDad...\x02",
    )

    CloseMessageWindow()

    label("loc_ACB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AEE")

    ChrTalk(    #12
        0x102,
        "#1514F#1PDad...\x02",
    )

    CloseMessageWindow()

    label("loc_AEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B15")

    ChrTalk(    #13
        0x103,
        "#1534F#1PCassius...\x02",
    )

    CloseMessageWindow()

    label("loc_B15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B47")

    ChrTalk(    #14
        0x106,
        "#556F#1PHeh. Knew it'd be you.\x02",
    )

    CloseMessageWindow()

    label("loc_B47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B70")

    ChrTalk(    #15
        0x108,
        "#573F#1PThought so...\x02",
    )

    CloseMessageWindow()

    label("loc_B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(    #16
        0x10E,
        "#179F#1PI feared as much...\x02",
    )

    CloseMessageWindow()

    label("loc_B9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC6")

    ChrTalk(    #17
        0x105,
        "#1382F#1PCassius...\x02",
    )

    CloseMessageWindow()

    label("loc_BC6")

    Sleep(300)
    Fade(1000)
    OP_6D(60510, 0, 70550, 0)
    OP_67(0, 4470, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(307, 0)

    def lambda_C13():
        OP_8F(0xFE, 0xE362, 0x0, 0x10536, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C13)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C99")

    def lambda_C41():
        OP_8F(0xFE, 0xE934, 0x0, 0x105B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_C41)
    Sleep(100)

    def lambda_C61():
        OP_8F(0xFE, 0xE13C, 0x0, 0xFDF2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_C61)
    Sleep(100)

    def lambda_C81():
        OP_8F(0xFE, 0xE8E4, 0x0, 0xFE4B, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_C81)
    Jump("loc_D6E")

    label("loc_C99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D05")

    def lambda_CAD():
        OP_8F(0xFE, 0xE934, 0x0, 0x105B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_CAD)
    Sleep(100)

    def lambda_CCD():
        OP_8F(0xFE, 0xE13C, 0x0, 0xFDF2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_CCD)
    Sleep(100)

    def lambda_CED():
        OP_8F(0xFE, 0xE8E4, 0x0, 0xFE4B, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_CED)
    Jump("loc_D6E")

    label("loc_D05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6E")

    def lambda_D19():
        OP_8F(0xFE, 0xE934, 0x0, 0x105B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_D19)
    Sleep(100)

    def lambda_D39():
        OP_8F(0xFE, 0xE13C, 0x0, 0xFDF2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_D39)
    Sleep(100)

    def lambda_D59():
        OP_8F(0xFE, 0xE8E4, 0x0, 0xFE4B, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_D59)

    label("loc_D6E")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x10,
        (
            "#1125F#5PHmm... I thought the ordeal revolving around\x01",
            "the Aureole was over.\x02\x03",

            "But it looks like that was premature of me.\x02\x03",

            "#1122FI doubt even Ragnard saw this coming.\x02\x03",

            "What about you and the Gralsritter, Kevin?\x01",
            "Did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1065F#6PNope. It took us completely by surprise.\x02\x03",

            "#1840FAlthough, I can't say for sure whether the bigwigs\x01",
            "at the top of the Congregation for the Sacraments\x01",
            "had any idea this might happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#1128F#5PI do wonder...\x02\x03",

            "#1123FWell, I suppose there's no point in debating\x01",
            "that now, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x42E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 2)
    OP_0D()
    Sleep(500)
    Fade(500)

    def lambda_FEF():
        OP_6D(60510, 0, 71000, 500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_FEF)

    def lambda_1007():
        OP_6B(2800, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1007)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_22(0xD5, 0x0, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x10,
        (
            "#1125F#5PLet's get down to business. As you know,\x01",
            "I'm the third of the guardians.\x02\x03",

            "#1122FIf you defeat me, you can move on. If you can't, \x01",
            "the road ahead will remain forever closed.\x02\x03",

            "Of course, you already know as much, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10C,
        (
            "#110F#12PIndeed. We came fully resolved to deal with what\x01",
            "we knew was waiting for us.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 11)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 13)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 15)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(600)

    ChrTalk(    #23
        0x10C,
        (
            "#115F#12PDefeating you will allow me to finally cut down my\x01",
            "hesitations and move forward...\x02\x03",

            "#112F...and for that reason, I will hold back nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#1120F#5PThat's what I wanted to hear.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15E2")
    Sleep(500)

    ChrTalk(    #25
        0x10,
        (
            "#1123F#5PStill, I wasn't expecting the two of you to get\x01",
            "dragged into this with you out of the country.\x02\x03",

            "#1120FI've been reading all the letters you send me...\x01",
            "How are the two of you doing? Good?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13F2")

    ChrTalk(    #26
        0x101,
        "#1016F#12PHeehee. We're both doing great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#1501F#12PI'm glad to see you look well, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14C4")

    label("loc_13F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_145D")

    ChrTalk(    #28
        0x101,
        (
            "#1012F#12PHeehee. We're both doing great.\x02\x03",

            "#1008FI'm glad to see you look well, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C4")

    label("loc_145D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C4")

    ChrTalk(    #29
        0x102,
        (
            "#1513F#12PWe're both doing fine, thanks.\x02\x03",

            "#1501FI'm glad to see you look well, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C4")


    ChrTalk(    #30
        0x10,
        (
            "#1125F#5PI'm not planning on letting age get the better\x01",
            "of me yet!\x02\x03",

            "#1120FEither way, this will be a good chance to show\x01",
            "me how much you've improved since you left on\x01",
            "your trip. I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15BA")

    ChrTalk(    #31
        0x101,
        "#1017F#12PRight!\x02",
    )

    CloseMessageWindow()

    label("loc_15BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E2")

    ChrTalk(    #32
        0x102,
        "#1514F#12POf course!\x02",
    )

    CloseMessageWindow()

    label("loc_15E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_174F")
    Sleep(500)

    ChrTalk(    #33
        0x10,
        (
            "#1124F#5PDamn, though. I almost didn't recognize you, \x01",
            "there, Scherazard.\x02\x03",

            "#1120FWhen did you cut your hair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x103,
        (
            "#1521F#12PHaha. About a month ago, I guess?\x02\x03",

            "#1527FI'd forgotten you hadn't seen me like this yet.\x02\x03",

            "Hopefully, I'll be able to surprise you by just how\x01",
            "much stronger I've been able to become, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        "#1120F#5PI hope so, too.\x02",
    )

    CloseMessageWindow()

    label("loc_174F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18FC")
    Sleep(500)

    ChrTalk(    #36
        0x106,
        (
            "#051F#12PAll right, old man. I might not've stood a chance\x01",
            "against you before, but today's different.\x02\x03",

            "#053FBack when I first met you, I didn't really get the\x01",
            "true meaning of what it was to swing this heavy\x01",
            "blade of mine around...\x02\x03",

            "#054F...but not anymore! Now it's time for you to learn \x01",
            "just how much this thing hurts when it's swung by\x01",
            "someone who knows how to use it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        "#1125F#5PHeh. Good to hear.\x02",
    )

    CloseMessageWindow()

    label("loc_18FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B68")
    Sleep(500)

    ChrTalk(    #38
        0x10E,
        (
            "#179F#12PI'm honored to have the chance to test my\x01",
            "skills against you again, Brigadier General.\x02\x03",

            "#170FI'd like to believe I will be able to fare better\x01",
            "against you than I did during our last battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#1125F#5POh, I'm sure you will. I'm looking forward to seeing\x01",
            "how much.\x02\x03",

            "#1120FI may have taught you the basics of swordsmanship,\x01",
            "but it's clear you've long moved on beyond those\x01",
            "and started to develop your own style.\x02\x03",

            "So I hope you will continue to follow the path you\x01",
            "believe in. I'm sure it won't lead you astray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10E,
        (
            "#171F#12PThank you, sir. I'm honored you would speak so\x01",
            "highly of me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DCE")
    Sleep(500)

    ChrTalk(    #41
        0x10,
        (
            "#1120F#5PI always seem to end up causing you trouble,\x01",
            "don't I, Zin? Sorry about that.\x02\x03",

            "#1123FAlthough you being here doesn't surprise me half\x01",
            "as much as Kilika ending up being drawn into all\x01",
            "of this! I thought she'd gone back home for good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x108,
        (
            "#573F#12PAhh, don't worry about it. It's clearly just fate\x01",
            "messing with us.\x02\x03",

            "#070FStill, I intend to make the most of this chance\x01",
            "to test my skills.\x02\x03",

            "I'm eager to know just how far my fists can take\x01",
            "me against a true master like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#1125F#5PHah. By all means.\x02\x03",

            "#1120FI'm looking forward to seeing the heights of\x01",
            "the Taito school myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F79")
    Sleep(500)

    ChrTalk(    #44
        0x10A,
        (
            "#819F#12PAhaha... I never thought I'd get the chance to\x01",
            "fight you like this...\x02\x03",

            "#816FSo, like...you know. I'll do my best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#1125F#5PHaha. I almost wish I would've had the chance\x01",
            "to fight you back before I abandoned the path\x01",
            "of the sword.\x02\x03",

            "#1120FBut knowing how you learned your skills from\x01",
            "Master Ka-fai himself, I'm looking forward to\x01",
            "seeing firsthand what you can do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10A,
        "#1310F#12PSame to you!\x02",
    )

    CloseMessageWindow()

    label("loc_1F79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2181")
    Sleep(500)

    ChrTalk(    #47
        0x10,
        (
            "#1125F#5PIncidentally, if I may, Princess Klaudia...\x02\x03",

            "#1122FI don't suppose I would be able to ask you to\x01",
            "step aside and have someone else fight in your\x01",
            "place, would I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#1383F#12PI'm afraid that won't be possible.\x02\x03",

            "#1160FI doubt I could defeat you in a battle of swords,\x01",
            "but I do have confidence in my ability to use arts\x01",
            "to fight and support my friends.\x02\x03",

            "So I have no intention of stepping aside and every\x01",
            "intention of helping everyone here on to victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        "#1125F#5P...Very well, then.\x02",
    )

    CloseMessageWindow()

    label("loc_2181")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2350")
    Sleep(500)

    ChrTalk(    #50
        0x10,
        (
            "#1123F#5PAs for you, Prince Olivert...I'm surprised you\x01",
            "came to fight me yourself.\x02\x03",

            "Surely you could've let the others take care\x01",
            "of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x104,
        (
            "#1541F#12PAnd pass up such a valuable opportunity?\x02\x03",

            "#1540FWhether I fight you or not, a battle with the\x01",
            "Empire's greatest monster is in my future...\x01",
            "I need all the experience I can get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        (
            "#1120F#5PThat's a fair point, I suppose. I guess I really\x01",
            "can't afford to let my guard down against you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2350")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24E0")
    Sleep(500)

    ChrTalk(    #53
        0x10D,
        (
            "#278F#12PIt's an honor to be able to test my skills against\x01",
            "you, Brigadier General Bright.\x02\x03",

            "#277FI look forward to seeing what you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#1125F#5PI could say the same to you, young lion of the\x01",
            "Vanders.\x02\x03",

            "#1120FYour family is held in high esteem both inside\x01",
            "Erebonia and outside it, so I'm very curious to\x01",
            "see what you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10D,
        "#275F#12PI hope not to disappoint you.\x02",
    )

    CloseMessageWindow()

    label("loc_24E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2679")
    Sleep(500)

    ChrTalk(    #56
        0x10,
        (
            "#1120F#5PBy the way, Tita...\x02\x03",

            "Is it true your parents have come home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x107,
        (
            "#067F#12POh! Yes, it is. Just recently.\x02\x03",

            "#560FDo you know my mom and dad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#1125F#5PI do. Your father in particular--he helped me\x01",
            "out an awful lot back during my early days of\x01",
            "being a bracer.\x02\x03",

            "#1120FThey must be pretty worried about you...\x01",
            "All the more reason you have to return safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x107,
        "#066F#12PYep!\x02",
    )

    CloseMessageWindow()

    label("loc_2679")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2845")
    Sleep(500)

    ChrTalk(    #60
        0x10,
        (
            "#1123F#5PNow, if there's one face I didn't expect to see\x01",
            "here, it's yours.\x02\x03",

            "#1120FHow fares the delivery service? Business booming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10B,
        (
            "#210F#12PExploding, even. Thanks for asking.\x02\x03",

            "At the rate we're going, it shouldn't be too long\x01",
            "before we're able to repay our debt to Her Majesty\x01",
            "off in full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "#1120F#5PHeh. All the more reason why you need to get out\x01",
            "of here safely and get back to work, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10B,
        "#413F#12PYou're telling me.\x02",
    )

    CloseMessageWindow()

    label("loc_2845")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A88")
    Sleep(500)

    ChrTalk(    #64
        0x110,
        "#262F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        "#1124F#5PHmm? What's with the funny stare, young lady?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x110,
        (
            "#268F#12PYou're a real monster, aren't you?\x02\x03",

            "#1302FI should be able to sense how strong you are...\x01",
            "Why can't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        (
            "#1120F#5PHaha... I manipulate both the void and the helix \x01",
            "as my form.\x02\x03",

            "You might be a genius, but even you won't be\x01",
            "able to get a handle on my capabilities so easily.\x02\x03",

            "#1121FAnd while I've got the chance, you should drop\x01",
            "by our house with Estelle and Joshua some time.\x02\x03",

            "We'd welcome you with open arms!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x110,
        "#1308F#12PA-And why would I ever want to do that?!\x02",
    )

    CloseMessageWindow()

    label("loc_2A88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F40")
    Sleep(500)

    ChrTalk(    #69
        0x10F,
        (
            "#1447F#12PIt's good to have the chance to meet you, \x01",
            "Divine Blade.\x02\x03",

            "#1448FMy name is Ries Argent, a squire of the \x01",
            "Gralsritter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "#1124F#5PArgent?\x02\x03",

            "#1125F...You're Rufina's younger sister, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10F,
        (
            "#1444F#12PSir...?\x02\x03",

            "You've met Rufina?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#1120F#5PNot in person.\x02\x03",

            "But her name was known by a small portion of\x01",
            "those in the Bracer Guild, myself included.\x02\x03",

            "#1125FShe was known as perhaps the most skilled \x01",
            "negotiator in the whole of the church and an\x01",
            "expert at problem solving.\x02\x03",

            "In many ways, her way of doing things seemed\x01",
            "more akin to a bracer's than a knight's.\x02\x03",

            "#1122FShe was known as the Thousand Arms, I believe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x109,
        (
            "#1065F#12PIndeed...and what you've heard about her was\x01",
            "true, too.\x02\x03",

            "#1840FI heard at one point there were even talks about\x01",
            "the guild trying to get her to leave the church\x01",
            "and join them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "#1120F#5POh, I can confirm as much. As long as she\x01",
            "wasn't a Dominion, we figured the chances of\x01",
            "her joining weren't zero and it was worth a shot.\x02\x03",

            "#1125FUnfortunately, she lost her life before those\x01",
            "negotiations could seriously get going.\x02\x03",

            "I'm sorry for your loss. She was quite the woman,\x01",
            "by the sounds of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10F,
        "#1806F#12P...Thank you for your kind words.\x02",
    )

    CloseMessageWindow()

    label("loc_2F40")


    def lambda_2F46():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2F46)
    OP_1D(0x77)
    Sleep(1500)

    ChrTalk(    #76
        0x10,
        (
            "#1125F#5PWell, I think that's enough talking. It's time we\x01",
            "got started.\x02\x03",

            "#1122FAs I'm sure you understand already, I couldn't \x01",
            "hold back even if I wanted to.\x02\x03",

            "So, Richard, I have only one thing to say to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10C,
        "#112F#12P...Yes, sir.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_44(0xEE, 0x0)
    Fade(500)
    OP_6D(59010, 0, 75600, 0)
    OP_67(0, 2890, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(0, 0)
    OP_6E(352, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_309E():

        label("loc_309E")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_309E")

    QueueWorkItem2(0x109, 0, lambda_309E)

    def lambda_30B9():
        OP_6D(59010, 0, 74600, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_30B9)

    def lambda_30D1():
        OP_67(0, 2600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_30D1)

    def lambda_30E9():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_30E9)

    def lambda_30F9():
        OP_6E(345, 4000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_30F9)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 52)
    SetChrFlags(0x10, 0x800)
    SetChrFlags(0x10, 0x2)
    SetChrPos(0x10, 58980, 0, 73020, 180)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x109, 58270, 0, 66820, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B9")
    SetChrPos(0xEF, 59820, 0, 66810, 0)
    SetChrPos(0xF0, 57690, 0, 64819, 0)
    SetChrPos(0xF1, 60270, 0, 64819, 0)
    Jump("loc_323E")

    label("loc_31B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31FD")
    SetChrPos(0xF0, 59820, 0, 66810, 0)
    SetChrPos(0xEF, 57690, 0, 64819, 0)
    SetChrPos(0xF1, 60270, 0, 64819, 0)
    Jump("loc_323E")

    label("loc_31FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_323E")
    SetChrPos(0xF1, 59820, 0, 66810, 0)
    SetChrPos(0xEF, 57690, 0, 64819, 0)
    SetChrPos(0xF0, 60270, 0, 64819, 0)

    label("loc_323E")

    OP_0D()
    Sleep(500)
    OP_22(0x7E, 0x1, 0x64)

    def lambda_324F():

        label("loc_324F")

        OP_99(0xFE, 0x38, 0x3B, 0x5DC)
        OP_48()
        Jump("loc_324F")

    QueueWorkItem2(0x10, 2, lambda_324F)
    WaitChrThread(0xEE, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_23(0x85)

    def lambda_3278():
        OP_6D(59010, 0, 74460, 100)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3278)

    def lambda_3290():
        OP_67(0, 2600, -10000, 100)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3290)

    def lambda_32A8():
        OP_6B(2850, 100)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_32A8)

    def lambda_32B8():
        OP_6E(341, 100)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_32B8)
    OP_23(0x7E)
    OP_44(0x10, 0x2)

    def lambda_32CF():
        OP_99(0xFE, 0x40, 0x46, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_32CF)
    OP_22(0x1F4, 0x0, 0x64)
    Sleep(100)
    OP_22(0xF3, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x10, 0x3)
    OP_44(0x109, 0x0)
    Sleep(1000)

    ChrTalk(    #78
        0x10,
        (
            "#1125F#5PDefeat me.#2040W #20W \x01",
            "#1122FThat is all.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #79
        0x10C,
        "#114F#6P#3SI shall!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(100)
    Battle(0x2AA, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_680 end

    def Function_7_3366(): pass

    label("Function_7_3366")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    Sleep(1000)
    OP_1D(0xAD)
    SetMapFlags(0x2000000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E0(238, 0x49, 0x2)
    OP_E0(238, 0x4A, 0x5)
    OP_E0(239, 0x4B, 0x2)
    OP_E0(239, 0x4C, 0x5)
    OP_E0(240, 0x4D, 0x2)
    OP_E0(240, 0x4E, 0x5)
    OP_E0(241, 0x4F, 0x2)
    OP_E0(241, 0x50, 0x5)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 58980, 0, 73020, 180)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x800)
    ClearChrFlags(0x10, 0x2)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x10, 0x3, 0x0, 0x8)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    PlayEffect(0x0, 0x0, 0x10, 100, 800, 100, 0, 0, 0, 2200, 3500, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x3C)
    SetChrPos(0x109, 57980, 0, 68490, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D1")
    SetChrPos(0xEF, 59450, 0, 68450, 0)
    SetChrPos(0xF0, 57410, 0, 66470, 0)
    SetChrPos(0xF1, 59260, 0, 66350, 0)
    Jump("loc_3556")

    label("loc_34D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3515")
    SetChrPos(0xF0, 59450, 0, 68450, 0)
    SetChrPos(0xEF, 57410, 0, 66470, 0)
    SetChrPos(0xF1, 59260, 0, 66350, 0)
    Jump("loc_3556")

    label("loc_3515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3556")
    SetChrPos(0xF1, 59450, 0, 68450, 0)
    SetChrPos(0xEF, 57410, 0, 66470, 0)
    SetChrPos(0xF0, 59260, 0, 66350, 0)

    label("loc_3556")

    SetChrChipByIndex(0xEE, 10)
    SetChrSubChip(0xEE, 3)
    SetChrChipByIndex(0xEF, 12)
    SetChrSubChip(0xEF, 3)
    SetChrChipByIndex(0xF0, 14)
    SetChrSubChip(0xF0, 3)
    SetChrChipByIndex(0xF1, 16)
    SetChrSubChip(0xF1, 3)
    SetChrFlags(0xEE, 0x800)
    SetChrFlags(0xEF, 0x800)
    SetChrFlags(0xF0, 0x800)
    SetChrFlags(0xF1, 0x800)
    OP_43(0xEE, 0x0, 0x0, 0x9)
    OP_43(0xEF, 0x0, 0x0, 0x9)
    OP_43(0xF0, 0x0, 0x0, 0x9)
    OP_43(0xF1, 0x0, 0x0, 0x9)
    OP_6D(60160, 0, 71550, 0)
    OP_67(0, 4090, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(45000, 0)
    OP_6E(306, 0)

    def lambda_35F1():
        OP_6B(2730, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_35F1)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #80
        0x109,
        (
            "#1070F#6PNgh... I think all those rumors about his\x01",
            "strength were underselling him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10C,
        (
            "#117F#12P*pant*...*pant*...\x01",
            "We did it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        (
            "#1125F#5PCongratulations. That was a well-earned \x01",
            "victory.\x02\x03",

            "#1122FSo, Richard? Have you finally been able\x01",
            "to clear aside your hesitations?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_44(0x0, 0x0)
    Sleep(50)
    OP_44(0x1, 0x0)
    Sleep(50)
    OP_44(0x2, 0x0)
    Sleep(50)
    OP_44(0x3, 0x0)
    Sleep(500)

    ChrTalk(    #83
        0x10C,
        (
            "#115F#12P...I believe so.\x02\x03",

            "No matter where life may end up taking me,\x01",
            "the swordsmanship I learned from you will\x01",
            "always have a place and a use.\x02\x03",

            "#111FAs such, I intend to keep following the path\x01",
            "I have chosen for myself, pride in my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        (
            "#1120F#5PWell said.\x02\x03",

            "#1123F...Although, I can't pretend not to be a tad \x01",
            "disappointed. If you'd returned to the army,\x01",
            "I could've piled all my work onto you and Cid.\x02\x03",

            "Looks like I'm not going to be able to retire\x01",
            "any time soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10C,
        (
            "#119F#12PHaha... I'm afraid not.\x02\x03",

            "#112FBut know this:\x02\x03",

            "As my final duty as a member of the military,\x01",
            "I will resolve this crisis and return everyone to\x01",
            "the real world.\x02\x03",

            "Have no doubt of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x10,
        "#1120F#5PI'll be counting on you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C03")
    Sleep(500)

    ChrTalk(    #87
        0x101,
        (
            "#1025F#12PDon't worry about us, either, Dad.\x02\x03",

            "Me and Joshua will get out of here safely.\x01",
            "We promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        "#1514F#12PYeah. We'll be just fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x10,
        (
            "#1125F#5POh, I'm sure you will.\x02\x03",

            "#1120FWhen you get out of here, you'll have to try \x01",
            "and find the time to pop back to Liberl from\x01",
            "time to time, too. I'll be happy to see you.\x02\x03",

            "#1121FMake sure to bring Renne with you, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1004F#12POh...\x02\x03",

            "#1017F...No problem!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        "#1501F#12PHaha. Look forward to it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ED1")

    label("loc_3C03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D5E")

    ChrTalk(    #92
        0x101,
        (
            "#1025F#12PDon't worry about us, either, Dad.\x02\x03",

            "Me and Joshua will get out of here,\x01",
            "so don't you worry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        (
            "#1125F#5POh, I'm sure you'll be just fine.\x02\x03",

            "#1120FWhen you get out of here, you'll have to try \x01",
            "and find the time to pop back to Liberl from\x01",
            "time to time, too. I'll be happy to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1017F#12PHeehee. We will!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ED1")

    label("loc_3D5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ED1")

    ChrTalk(    #95
        0x102,
        (
            "#1513F#12PDon't worry about us, either, Dad.\x01",
            "We'll be fine.\x02\x03",

            "#1514FI'll be sure Estelle gets out of here\x01",
            "safely. I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x10,
        (
            "#1125F#5POh, I'm sure the two of you will be just fine.\x02\x03",

            "#1120FWhen you get out of here, you'll have to try \x01",
            "and find the time to pop back to Liberl from\x01",
            "time to time, too. I'll be happy to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#1501F#12PWe will!\x02",
    )

    CloseMessageWindow()

    label("loc_3ED1")

    Sleep(500)

    ChrTalk(    #98
        0x10,
        (
            "#1125F#5PRegardless, my time here is short.\x02\x03",

            "#1122FSo I'll make this brief, Kevin.\x02\x03",

            "By now, you must have a fairly good idea\x01",
            "who the Lord of Phantasma is, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x109,
        (
            "#1840F#6PYeah... I just need one last push to be completely\x01",
            "certain.\x02\x03",

            "#1075FI'll probably get that push in the next area, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        (
            "#1128F#5P#40WI see...\x02\x03",

            "#1125F#40WIt's not really my place to say anything more\x01",
            "to you...\x02\x03",

            "#40W...so I would ask only that you not forget this.\x02\x03",

            "#1120F#40WNo man is an island; no matter how much they\x01",
            "may wish to isolate themselves from others,\x01",
            "no one can live their life truly alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        "#1079F#6P#3S...!!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, 100, -600, 0, 0, 0, 0, 2100, 2100, 2100, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_4195():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4195)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41E2")

    ChrTalk(    #102
        0x101,
        "#1026F#12POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_41E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4208")

    ChrTalk(    #103
        0x102,
        "#1504F#12POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_4208")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_422E")

    ChrTalk(    #104
        0x103,
        "#1523F#12POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_422E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4251")

    ChrTalk(    #105
        0x106,
        "#055F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_4251")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4274")

    ChrTalk(    #106
        0x108,
        "#072F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_4274")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4299")

    ChrTalk(    #107
        0x10E,
        "#173F#12POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_4299")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42BF")

    ChrTalk(    #108
        0x10A,
        "#1317F#12POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_42BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42E2")

    ChrTalk(    #109
        0x10D,
        "#273F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_42E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4307")

    ChrTalk(    #110
        0x110,
        "#264F#12POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_4307")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_432D")

    ChrTalk(    #111
        0x105,
        "#1163F#12POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_432D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4351")

    ChrTalk(    #112
        0x104,
        "#1543F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_4351")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4377")

    ChrTalk(    #113
        0x10F,
        "#1444F#12POh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_4377")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4399")

    ChrTalk(    #114
        0x10B,
        "#213F#12POh...\x02",
    )

    CloseMessageWindow()

    label("loc_4399")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43C3")

    ChrTalk(    #115
        0x107,
        "#063F#12PCassius...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_43C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43E6")

    ChrTalk(    #116
        0x10B,
        "#215F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_43E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_440A")

    ChrTalk(    #117
        0x10F,
        "#1445F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_440A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_442E")

    ChrTalk(    #118
        0x104,
        "#1542F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_442E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4459")

    ChrTalk(    #119
        0x105,
        "#1163F#12PCassius...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_4459")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_447D")

    ChrTalk(    #120
        0x110,
        "#1307F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_447D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44A0")

    ChrTalk(    #121
        0x10D,
        "#276F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_44A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44CA")

    ChrTalk(    #122
        0x10A,
        "#813F#12PCassius...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_44CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44FE")

    ChrTalk(    #123
        0x10E,
        "#175F#12PBrigadier General...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_44FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4521")

    ChrTalk(    #124
        0x108,
        "#572F#12P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_4521")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_454D")

    ChrTalk(    #125
        0x106,
        "#053F#12PHe's gone...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_454D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_457A")

    ChrTalk(    #126
        0x103,
        "#1532F#12PHe's gone...\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_457A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_459E")

    ChrTalk(    #127
        0x102,
        "#1503F#12PDad...\x02",
    )

    CloseMessageWindow()

    label("loc_459E")


    def lambda_45A4():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_45A4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M4110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_3366 end

    def Function_8_45C6(): pass

    label("Function_8_45C6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45E7")
    Sleep(100)
    Jump("loc_4662")

    label("loc_45E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45FC")
    Sleep(200)
    Jump("loc_4662")

    label("loc_45FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4611")
    Sleep(300)
    Jump("loc_4662")

    label("loc_4611")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4626")
    Sleep(400)
    Jump("loc_4662")

    label("loc_4626")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463B")
    Sleep(500)
    Jump("loc_4662")

    label("loc_463B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4650")
    Sleep(600)
    Jump("loc_4662")

    label("loc_4650")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4662")
    Sleep(700)

    label("loc_4662")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4684")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_4662")

    label("loc_4684")

    Return()

    # Function_8_45C6 end

    def Function_9_4685(): pass

    label("Function_9_4685")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_475D")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46AF")
    Sleep(100)
    Jump("loc_472A")

    label("loc_46AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46C4")
    Sleep(200)
    Jump("loc_472A")

    label("loc_46C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46D9")
    Sleep(300)
    Jump("loc_472A")

    label("loc_46D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46EE")
    Sleep(400)
    Jump("loc_472A")

    label("loc_46EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4703")
    Sleep(500)
    Jump("loc_472A")

    label("loc_4703")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4718")
    Sleep(600)
    Jump("loc_472A")

    label("loc_4718")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_472A")
    Sleep(700)

    label("loc_472A")

    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_9_4685")

    label("loc_475D")

    Return()

    # Function_9_4685 end

    def Function_10_475E(): pass

    label("Function_10_475E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 57980, 0, 68490, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47BF")
    SetChrPos(0xEF, 59650, 0, 68450, 0)
    SetChrPos(0xF0, 57410, 0, 66470, 0)
    SetChrPos(0xF1, 59260, 0, 66650, 0)
    Jump("loc_4844")

    label("loc_47BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4803")
    SetChrPos(0xF0, 59650, 0, 68450, 0)
    SetChrPos(0xEF, 57410, 0, 66470, 0)
    SetChrPos(0xF1, 59260, 0, 66650, 0)
    Jump("loc_4844")

    label("loc_4803")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4844")
    SetChrPos(0xF1, 59650, 0, 68450, 0)
    SetChrPos(0xEF, 57410, 0, 66470, 0)
    SetChrPos(0xF0, 59260, 0, 66650, 0)

    label("loc_4844")

    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_6D(60000, 0, 71900, 0)
    OP_67(0, 4740, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #128
        0x10C,
        "#116F#5P...\x02",
    )

    CloseMessageWindow()

    def lambda_48D9():
        OP_6D(60000, 0, 68900, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_48D9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4929")

    def lambda_48FF():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_48FF)
    Sleep(300)

    def lambda_4912():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4912)
    Sleep(100)
    OP_8C(0xF0, 45, 400)
    Jump("loc_49A2")

    label("loc_4929")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4967")

    def lambda_493D():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_493D)
    Sleep(300)

    def lambda_4950():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4950)
    Sleep(100)
    OP_8C(0xEF, 45, 400)
    Jump("loc_49A2")

    label("loc_4967")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49A2")

    def lambda_497B():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_497B)
    Sleep(300)

    def lambda_498E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_498E)
    Sleep(100)
    OP_8C(0xEF, 45, 400)

    label("loc_49A2")

    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #129
        0x10C,
        (
            "#111F#5PWell, we have but one area remaining now.\x02\x03",

            "#119FAfter what we have accomplished here, I'm not\x01",
            "sure we have anything to fear.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A64")

    ChrTalk(    #130
        0x101,
        "#1016F#6PAhaha... Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4A64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A8B")

    ChrTalk(    #131
        0x102,
        "#1513F#6PYeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4A8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AB8")

    ChrTalk(    #132
        0x103,
        "#1521F#6PHaha. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4AB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AE7")

    ChrTalk(    #133
        0x106,
        "#556F#6PHeh. Damn right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4AE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B13")

    ChrTalk(    #134
        0x108,
        "#573F#6PHaha. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4B13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B42")

    ChrTalk(    #135
        0x105,
        "#1165F#6PHeehee. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4B42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B6D")

    ChrTalk(    #136
        0x10E,
        "#179F#6PHeh. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4B6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B9B")

    ChrTalk(    #137
        0x10A,
        "#1314F#6PAhaha... Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4B9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BC7")

    ChrTalk(    #138
        0x104,
        "#1545F#6PHeh. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4BC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BF2")

    ChrTalk(    #139
        0x10D,
        "#278F#6PHeh. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4BF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C1D")

    ChrTalk(    #140
        0x107,
        "#067F#6PHeehee. Yup!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4C1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C4C")

    ChrTalk(    #141
        0x10F,
        "#1447F#6PHeehee. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_4C4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C79")

    ChrTalk(    #142
        0x110,
        "#263F#6PThat's very true.\x02",
    )

    CloseMessageWindow()

    label("loc_4C79")


    ChrTalk(    #143
        0x109,
        (
            "#1075F#6PLet's head back to the scenic route and\x01",
            "check the final monument.\x02\x03",

            "#1840FThat way we can find out what the condition\x01",
            "for opening it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x2B20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D33")
    OP_A2(0x2639)

    label("loc_4D33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D44")
    OP_A2(0x263A)

    label("loc_4D44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D55")
    OP_A2(0x263B)

    label("loc_4D55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D66")
    OP_A2(0x263C)

    label("loc_4D66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D77")
    OP_A2(0x263D)

    label("loc_4D77")

    OP_28(0x3A, 0x4, 0x4)
    OP_28(0x3A, 0x4, 0x8)
    OP_28(0x3A, 0x1, 0x1)
    OP_6D(58950, 0, 68910, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 58950, 0, 68910, 180)
    SetChrPos(0x1, 58950, 0, 68910, 180)
    SetChrPos(0x2, 58950, 0, 68910, 180)
    SetChrPos(0x3, 58950, 0, 68910, 180)
    OP_21()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_1D(0xE8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000000)
    EventEnd(0x0)
    Return()

    # Function_10_475E end

    def Function_11_4E2A(): pass

    label("Function_11_4E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF9")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(6912)
    Sleep(500)
    Jump("loc_4EFC")

    label("loc_4EF9")

    TalkBegin(0xFF)

    label("loc_4EFC")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #144
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_507B")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F94"),
        (1, "loc_500F"),
        (2, "loc_503D"),
        (SWITCH_DEFAULT, "loc_506B"),
    )


    label("loc_4F94")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE8)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5078")

    label("loc_500F")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #145
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_5078")

    label("loc_503D")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #146
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_5078")

    label("loc_506B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5078")

    label("loc_5078")

    Jump("loc_4F38")

    label("loc_507B")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50A8")
    OP_A2(0x259D)
    EventEnd(0x1)
    Jump("loc_50AB")

    label("loc_50A8")

    TalkEnd(0xFF)

    label("loc_50AB")

    Return()

    # Function_11_4E2A end

    SaveToFile()

Try(main)
