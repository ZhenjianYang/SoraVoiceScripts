from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7201   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60223",
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
        'ED6_DT29/CH14470 ._CH',             # 00
        'ED6_DT29/CH14471 ._CH',             # 01
        'ED6_DT29/CH15050 ._CH',             # 02
        'ED6_DT29/CH15051 ._CH',             # 03
        'ED6_DT29/CH15060 ._CH',             # 04
        'ED6_DT29/CH15061 ._CH',             # 05
        'ED6_DT29/CH14480 ._CH',             # 06
        'ED6_DT29/CH14481 ._CH',             # 07
        'ED6_DT29/CH14490 ._CH',             # 08
        'ED6_DT29/CH14491 ._CH',             # 09
        'ED6_DT29/CH14560 ._CH',             # 0A
        'ED6_DT29/CH14561 ._CH',             # 0B
        'ED6_DT29/CH14010 ._CH',             # 0C
        'ED6_DT29/CH14011 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH14470P._CP',             # 00
        'ED6_DT29/CH14471P._CP',             # 01
        'ED6_DT29/CH15050P._CP',             # 02
        'ED6_DT29/CH15051P._CP',             # 03
        'ED6_DT29/CH15060P._CP',             # 04
        'ED6_DT29/CH15061P._CP',             # 05
        'ED6_DT29/CH14480P._CP',             # 06
        'ED6_DT29/CH14481P._CP',             # 07
        'ED6_DT29/CH14490P._CP',             # 08
        'ED6_DT29/CH14491P._CP',             # 09
        'ED6_DT29/CH14560P._CP',             # 0A
        'ED6_DT29/CH14561P._CP',             # 0B
        'ED6_DT29/CH14010P._CP',             # 0C
        'ED6_DT29/CH14011P._CP',             # 0D
    )

    DeclMonster(
        X                   = -33960,
        Z                   = 750,
        Y                   = 20090,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 29720,
        Z                   = -7200,
        Y                   = 31730,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 29210,
        Z                   = -6800,
        Y                   = 44130,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1FA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -120,
        Z                   = -3200,
        Y                   = 34110,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -130,
        Z                   = 750,
        Y                   = 81960,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -140,
        TriggerZ            = 4800,
        TriggerY            = 131920,
        TriggerRange        = 1000,
        ActorX              = -140,
        ActorZ              = 6800,
        ActorY              = 131920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -34000,
        TriggerZ            = 750,
        TriggerY            = 20000,
        TriggerRange        = 1000,
        ActorX              = -34000,
        ActorZ              = 1750,
        ActorY              = 20000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -2800,
        TriggerY            = 19000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -1800,
        ActorY              = 19000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41650,
        TriggerZ            = 750,
        TriggerY            = 81800,
        TriggerRange        = 1000,
        ActorX              = -41650,
        ActorZ              = 1750,
        ActorY              = 81800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_236",          # 00, 0
        "Function_1_2AB",          # 01, 1
        "Function_2_355",          # 02, 2
        "Function_3_4BC",          # 03, 3
        "Function_4_6B9",          # 04, 4
        "Function_5_7D6",          # 05, 5
        "Function_6_8E2",          # 06, 6
        "Function_7_B64",          # 07, 7
        "Function_8_C42",          # 08, 8
        "Function_9_D20",          # 09, 9
        "Function_10_DFE",         # 0A, 10
        "Function_11_EDC",         # 0B, 11
        "Function_12_FBA",         # 0C, 12
        "Function_13_1098",        # 0D, 13
        "Function_14_1176",        # 0E, 14
        "Function_15_1232",        # 0F, 15
        "Function_16_12EE",        # 10, 16
        "Function_17_13AA",        # 11, 17
        "Function_18_1466",        # 12, 18
        "Function_19_1522",        # 13, 19
        "Function_20_15DE",        # 14, 20
        "Function_21_169A",        # 15, 21
        "Function_22_17B0",        # 16, 22
    )


    def Function_0_236(): pass

    label("Function_0_236")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_297")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_266"),
        (101, "loc_26D"),
        (102, "loc_274"),
        (103, "loc_27B"),
        (104, "loc_282"),
        (105, "loc_289"),
        (106, "loc_290"),
        (SWITCH_DEFAULT, "loc_297"),
    )


    label("loc_266")

    Event(0, 7)
    Jump("loc_297")

    label("loc_26D")

    Event(0, 12)
    Jump("loc_297")

    label("loc_274")

    Event(0, 11)
    Jump("loc_297")

    label("loc_27B")

    Event(0, 8)
    Jump("loc_297")

    label("loc_282")

    Event(0, 9)
    Jump("loc_297")

    label("loc_289")

    Event(0, 10)
    Jump("loc_297")

    label("loc_290")

    Event(0, 13)
    Jump("loc_297")

    label("loc_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2AA")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_2AA")

    Return()

    # Function_0_236 end

    def Function_1_2AB(): pass

    label("Function_1_2AB")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFF63C0, 0x23008C)
    OP_1B(0x0, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0x13)
    OP_1B(0x2, 0x0, 0x12)
    OP_1B(0x3, 0x0, 0xF)
    OP_1B(0x4, 0x0, 0x10)
    OP_1B(0x5, 0x0, 0x11)
    OP_1B(0x6, 0x0, 0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_2ED")
    OP_71(0x402, 0x0)
    ExitThread()

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_2FE")

    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B")
    OP_6F(0x5, 0)
    Jump("loc_322")

    label("loc_31B")

    OP_6F(0x5, 60)

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334")
    OP_6F(0x6, 0)
    Jump("loc_33B")

    label("loc_334")

    OP_6F(0x6, 60)

    label("loc_33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D")
    OP_6F(0x7, 0)
    Jump("loc_354")

    label("loc_34D")

    OP_6F(0x7, 60)

    label("loc_354")

    Return()

    # Function_1_2AB end

    def Function_2_355(): pass

    label("Function_2_355")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x581, 1)"), scpexpr(EXPR_END)), "loc_3C3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x81\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A88)
    Jump("loc_42B")

    label("loc_3C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x81\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x81\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_42B")

    Jump("loc_4AE")

    label("loc_42E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You hear some funky music playing from within the chest, but you do not\x01",
            "see any instruments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xD1, 0x0)

    label("loc_4AE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_355 end

    def Function_3_4BC(): pass

    label("Function_3_4BC")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x1E)
    OP_73(0x6)
    OP_6F(0x6, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #3
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x200\x01",
            "#57IWater Sepith x200\x01",
            "#58IFire Sepith x200\x01",
            "#59IWind Sepith x200\x01",
            "#62ITime Sepith x200\x01",
            "#60ISpace Sepith x200\x01",
            "#61IMirage Sepith x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2A89)
    Jump("loc_6A2")

    label("loc_5CC")


    AnonymousTalk(    #4
        (
            "\x07\x05Their was wants an air too a kingdom who aloud everyone a peace of\x01",
            "meet from a bore and up of whine; provided, of coarse, they found the\x01",
            "quay to his secret seller underground. Finding it was know mein feet.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_6A2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xD2, 0x0)
    Return()

    # Function_3_4BC end

    def Function_4_6B9(): pass

    label("Function_4_6B9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x551, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_792")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x476, 1)"), scpexpr(EXPR_END)), "loc_727")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Found \x1F\x76\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A8A)
    Jump("loc_78F")

    label("loc_727")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05Found \x1F\x76\x04\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x76\x04\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_78F")

    Jump("loc_7C8")

    label("loc_792")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Cry into my chest.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xD3, 0x0)

    label("loc_7C8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6B9 end

    def Function_5_7D6(): pass

    label("Function_5_7D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xEE, 0x80)
    SetChrFlags(0xEF, 0x80)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(1680, 5200, 138300, 0)
    OP_67(0, 8970, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(428, 0)

    def lambda_839():
        OP_6D(-300, 8100, 157570, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_839)

    def lambda_851():
        OP_67(0, 1570, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_851)

    def lambda_869():
        OP_6B(3620, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_869)

    def lambda_879():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_879)

    def lambda_889():
        OP_6E(398, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_889)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)
    Fade(1000)

    def lambda_8AD():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8AD)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2505)
    OP_A2(0x2506)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_7D6 end

    def Function_6_8E2(): pass

    label("Function_6_8E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B1")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(4096)
    Sleep(500)
    Jump("loc_9B4")

    label("loc_9B1")

    TalkBegin(0xFF)

    label("loc_9B4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #8
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B33")

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
        (0, "loc_A4C"),
        (1, "loc_AC7"),
        (2, "loc_AF5"),
        (SWITCH_DEFAULT, "loc_B23"),
    )


    label("loc_A4C")

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
    OP_1D(0xDF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B30")

    label("loc_AC7")

    OP_A9(0x22)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #9
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_B30")

    label("loc_AF5")

    OP_A9(0x8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #10
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_B30")

    label("loc_B23")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B30")

    label("loc_B30")

    Jump("loc_9F0")

    label("loc_B33")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B60")
    OP_A2(0x2593)
    EventEnd(0x1)
    Jump("loc_B63")

    label("loc_B60")

    TalkEnd(0xFF)

    label("loc_B63")

    Return()

    # Function_6_8E2 end

    def Function_7_B64(): pass

    label("Function_7_B64")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -120, 820, -220, 180)
    SetChrPos(0x1, -120, 820, -220, 180)
    SetChrPos(0x2, -120, 820, -220, 180)
    SetChrPos(0x3, -120, 820, -220, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -120, 820, -220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_7_B64 end

    def Function_8_C42(): pass

    label("Function_8_C42")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 37790, -3260, 81910, 270)
    SetChrPos(0x1, 37790, -3260, 81910, 270)
    SetChrPos(0x2, 37790, -3260, 81910, 270)
    SetChrPos(0x3, 37790, -3260, 81910, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 37790, -3260, 81910, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_8_C42 end

    def Function_9_D20(): pass

    label("Function_9_D20")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -40110, -3580, 110020, 90)
    SetChrPos(0x1, -40110, -3580, 110020, 90)
    SetChrPos(0x2, -40110, -3580, 110020, 90)
    SetChrPos(0x3, -40110, -3580, 110020, 90)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -40110, -3580, 110020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_9_D20 end

    def Function_10_DFE(): pass

    label("Function_10_DFE")

    OP_DE(0x0, 0x5, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 41500, 420, 109700, 270)
    SetChrPos(0x1, 41500, 420, 109700, 270)
    SetChrPos(0x2, 41500, 420, 109700, 270)
    SetChrPos(0x3, 41500, 420, 109700, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41500, 420, 109700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_10_DFE end

    def Function_11_EDC(): pass

    label("Function_11_EDC")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 25800, 4820, 131950, 270)
    SetChrPos(0x1, 25800, 4820, 131950, 270)
    SetChrPos(0x2, 25800, 4820, 131950, 270)
    SetChrPos(0x3, 25800, 4820, 131950, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 25800, 4820, 131950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_EDC end

    def Function_12_FBA(): pass

    label("Function_12_FBA")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -26000, 4820, 132000, 90)
    SetChrPos(0x1, -26000, 4820, 132000, 90)
    SetChrPos(0x2, -26000, 4820, 132000, 90)
    SetChrPos(0x3, -26000, 4820, 132000, 90)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -26000, 4820, 132000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_12_FBA end

    def Function_13_1098(): pass

    label("Function_13_1098")

    OP_DE(0x0, 0x6, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 110, 5370, 171840, 180)
    SetChrPos(0x1, 110, 5370, 171840, 180)
    SetChrPos(0x2, 110, 5370, 171840, 180)
    SetChrPos(0x3, 110, 5370, 171840, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 5370, 172000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_13_1098 end

    def Function_14_1176(): pass

    label("Function_14_1176")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -120, 820, -220, 0)
    SetChrPos(0x2, -120, 820, -220, 0)
    SetChrPos(0x1, -120, 820, -220, 0)
    SetChrPos(0x0, -120, 820, -220, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -120, 820, -220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7200   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1176 end

    def Function_15_1232(): pass

    label("Function_15_1232")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 37790, -3260, 81910, 90)
    SetChrPos(0x2, 37790, -3260, 81910, 90)
    SetChrPos(0x1, 37790, -3260, 81910, 90)
    SetChrPos(0x0, 37790, -3260, 81910, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 37790, -3260, 81910, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7201   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1232 end

    def Function_16_12EE(): pass

    label("Function_16_12EE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -40110, -3580, 110020, 270)
    SetChrPos(0x2, -40110, -3580, 110020, 270)
    SetChrPos(0x1, -40110, -3580, 110020, 270)
    SetChrPos(0x0, -40110, -3580, 110020, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -40110, -3580, 110020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7201   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_16_12EE end

    def Function_17_13AA(): pass

    label("Function_17_13AA")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 41500, 420, 109700, 90)
    SetChrPos(0x2, 41500, 420, 109700, 90)
    SetChrPos(0x1, 41500, 420, 109700, 90)
    SetChrPos(0x0, 41500, 420, 109700, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41500, 420, 109700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7200   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_17_13AA end

    def Function_18_1466(): pass

    label("Function_18_1466")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 25800, 4820, 131950, 90)
    SetChrPos(0x2, 25800, 4820, 131950, 90)
    SetChrPos(0x1, 25800, 4820, 131950, 90)
    SetChrPos(0x0, 25800, 4820, 131950, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 25800, 4820, 131950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7200   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1466 end

    def Function_19_1522(): pass

    label("Function_19_1522")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -26000, 4820, 132000, 270)
    SetChrPos(0x2, -26000, 4820, 132000, 270)
    SetChrPos(0x1, -26000, 4820, 132000, 270)
    SetChrPos(0x0, -26000, 4820, 132000, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -26000, 4820, 132000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7200   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1522 end

    def Function_20_15DE(): pass

    label("Function_20_15DE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 110, 5370, 171840, 0)
    SetChrPos(0x2, 110, 5370, 171840, 0)
    SetChrPos(0x1, 110, 5370, 171840, 0)
    SetChrPos(0x0, 110, 5370, 171840, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 5370, 172000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 22)
    NewScene("ED6_DT21/M7202   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_15DE end

    def Function_21_169A(): pass

    label("Function_21_169A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C3")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_16B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_16B7)

    label("loc_16C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16EC")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_16E0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_16E0)

    label("loc_16EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1715")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1709():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1709)

    label("loc_1715")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173E")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1732():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1732)

    label("loc_173E")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_176A")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_176A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1781")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1781")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1798")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1798")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17AF")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_17AF")

    Return()

    # Function_21_169A end

    def Function_22_17B0(): pass

    label("Function_22_17B0")


    def lambda_17B6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_17B6)

    def lambda_17C8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_17C8)

    def lambda_17DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_17DA)

    def lambda_17EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_17EC)
    Sleep(1000)
    Return()

    # Function_22_17B0 end

    SaveToFile()

Try(main)
