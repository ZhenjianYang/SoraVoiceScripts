from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2200.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60029",
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
        'Lucia',                                # 9
        'Grant',                                # 10
        'Manoria Village',                      # 11
        'Mercia Orphanage',                     # 12
        'Ruan',                                 # 13
        'Target Camera',                        # 14
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
        'ED6_DT07/CH01070 ._CH',             # 00
        'ED6_DT07/CH01260 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01070P._CP',             # 00
        'ED6_DT07/CH01260P._CP',             # 01
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -139370,
        Z                   = -2020,
        Y                   = 15120,
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
        X                   = -28630,
        Z                   = -1990,
        Y                   = 79340,
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
        X                   = 7410,
        Z                   = -2000,
        Y                   = 29980,
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


    DeclEvent(
        X                   = -126380,
        Y                   = -2900,
        Z                   = 18770,
        Range               = -124520,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x2C60,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = -114230,
        TriggerZ            = -6050,
        TriggerY            = 11770,
        TriggerRange        = 1000,
        ActorX              = -114730,
        ActorZ              = -6040,
        ActorY              = 12270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21830,
        TriggerZ            = -2000,
        TriggerY            = 37790,
        TriggerRange        = 1500,
        ActorX              = -21830,
        ActorZ              = -800,
        ActorY              = 37790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18840,
        TriggerZ            = -2000,
        TriggerY            = 33860,
        TriggerRange        = 1500,
        ActorX              = -18840,
        ActorZ              = -500,
        ActorY              = 33860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -82860,
        TriggerZ            = -6070,
        TriggerY            = 8950,
        TriggerRange        = 1500,
        ActorX              = -82860,
        ActorZ              = -5570,
        ActorY              = 8950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -88900,
        TriggerZ            = -6050,
        TriggerY            = 6520,
        TriggerRange        = 1500,
        ActorX              = -88900,
        ActorZ              = -5500,
        ActorY              = 6520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -96650,
        TriggerZ            = -5960,
        TriggerY            = 9640,
        TriggerRange        = 1500,
        ActorX              = -96650,
        ActorZ              = -5450,
        ActorY              = 9640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -96730,
        TriggerZ            = -6100,
        TriggerY            = 14600,
        TriggerRange        = 1500,
        ActorX              = -96730,
        ActorZ              = -5600,
        ActorY              = 14600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -101200,
        TriggerZ            = -6000,
        TriggerY            = 11000,
        TriggerRange        = 1500,
        ActorX              = -101200,
        ActorZ              = -5500,
        ActorY              = 11000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -54580,
        TriggerZ            = -1980,
        TriggerY            = 13860,
        TriggerRange        = 1500,
        ActorX              = -54580,
        ActorZ              = -980,
        ActorY              = 13860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2DE",          # 00, 0
        "Function_1_2DF",          # 01, 1
        "Function_2_3AE",          # 02, 2
        "Function_3_52B",          # 03, 3
        "Function_4_1791",         # 04, 4
        "Function_5_1829",         # 05, 5
        "Function_6_1842",         # 06, 6
        "Function_7_193E",         # 07, 7
        "Function_8_1D59",         # 08, 8
        "Function_9_1E22",         # 09, 9
        "Function_10_1EFC",        # 0A, 10
        "Function_11_200B",        # 0B, 11
        "Function_12_213E",        # 0C, 12
        "Function_13_224C",        # 0D, 13
        "Function_14_237A",        # 0E, 14
        "Function_15_2633",        # 0F, 15
        "Function_16_2732",        # 10, 16
        "Function_17_277C",        # 11, 17
    )


    def Function_0_2DE(): pass

    label("Function_0_2DE")

    Return()

    # Function_0_2DE end

    def Function_1_2DF(): pass

    label("Function_1_2DF")

    OP_16(0x2, 0xFA0, 0xFFFD21A0, 0xFFFE5638, 0x230026)
    OP_22(0x1C8, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308")
    OP_6F(0x0, 0)
    Jump("loc_30F")

    label("loc_308")

    OP_6F(0x0, 60)

    label("loc_30F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_338")
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_B2(0x0, 0x0, 0x80)

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_347")
    OP_64(0x8, 0x1)

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_353")
    OP_B2(0x0, 0x0, 0x80)

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_END)), "loc_35E")
    OP_64(0x3, 0x1)

    label("loc_35E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_END)), "loc_369")
    OP_64(0x4, 0x1)

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_END)), "loc_374")
    OP_64(0x5, 0x1)

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_END)), "loc_37F")
    OP_64(0x6, 0x1)

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_END)), "loc_38A")
    OP_64(0x7, 0x1)

    label("loc_38A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD")
    OP_1B(0x2, 0x0, 0xE)
    OP_71(0x1, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x201, 0x0)
    ExitThread()

    label("loc_3AD")

    Return()

    # Function_1_2DF end

    def Function_2_3AE(): pass

    label("Function_2_3AE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D3")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_515")

    label("loc_3D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_515")

    label("loc_3EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_405")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_515")

    label("loc_405")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41E")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_515")

    label("loc_41E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_515")

    label("loc_437")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_450")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_515")

    label("loc_450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_469")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_515")

    label("loc_469")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_515")

    label("loc_482")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_515")

    label("loc_49B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_515")

    label("loc_4B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CD")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_515")

    label("loc_4CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E6")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_515")

    label("loc_4E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_515")

    label("loc_4FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_515")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_515")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_515")

    label("loc_52A")

    Return()

    # Function_2_3AE end

    def Function_3_52B(): pass

    label("Function_3_52B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    SetChrPos(0x14E, -107740, -6000, 11600, 300)
    SetChrPos(0x14F, -106440, -6000, 14040, 200)
    SetChrFlags(0x14E, 0x40)
    SetChrFlags(0x14F, 0x40)
    OP_6D(-105600, -5400, 11820, 0)
    OP_67(0, 6800, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(306000, 0)
    OP_6E(282, 0)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    FadeToBright(2000, 0)

    def lambda_5C9():
        OP_6B(2520, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5C9)
    OP_43(0x14E, 0x2, 0x0, 0x4)
    OP_43(0x14F, 0x2, 0x0, 0x5)
    OP_0D()
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x14E, 0x2)

    ChrTalk(    #0
        0x14E,
        (
            "#1716FAww... It seemed like a good idea on paper,\x01",
            "but I can't do much with it without any nice\x01",
            "shells to use...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #1
        0x14E,
        (
            "#1900F...\x02\x03",

            "(I wish those happiness stones actually did\x01",
            "exist.)\x02\x03",

            "#1719F(One of those would be the perfect present\x01",
            "for the matron.)\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x14F, 0x2)

    def lambda_6F7():
        OP_6D(-105600, -5400, 11120, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6F7)

    def lambda_70F():
        OP_6B(2420, 1500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_70F)

    def lambda_71F():
        OP_8E(0xFE, 0xFFFE622C, 0xFFFFE890, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_71F)
    WaitChrThread(0x14F, 0x1)

    ChrTalk(    #2
        0x14F,
        (
            "#1733FWhat'cha thinking about, Mary?\x02\x03",

            "#1730FThat stone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x14E,
        "#1714FOh... Yeah...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 500)
    Sleep(500)

    ChrTalk(    #4
        0x14E,
        (
            "#1718FPolly? Do you think it's possible that\x01",
            "happiness stones might be real?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x14F,
        (
            "#1733FHuuuh?\x02\x03",

            "Do you want one so you can be happy?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #6
        0x14E,
        (
            "#1714FWell, that wasn't really what I meant...\x02\x03",

            "#1903FJust...don't you think it would be romantic\x01",
            "if something like that really existed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x14F,
        (
            "#1730F...\x02\x03",

            "#1732FHappiness is all around us.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x80, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -108400, -5540, 9800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8C(0x14F, 200, 400)
    Sleep(500)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14F, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)

    ChrTalk(    #8
        0x14F,
        "#1733FWhat's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x14E,
        "#1714FWhat?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 252, 400)
    Sleep(500)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)

    ChrTalk(    #10
        0x14E,
        "#1714FI don't know... It's really shiny, though.\x02",
    )

    CloseMessageWindow()

    def lambda_9EC():
        OP_6D(-108140, -5980, 10360, 1800)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_9EC)

    def lambda_A04():
        OP_6C(310000, 1800)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A04)

    def lambda_A14():
        OP_8E(0xFE, 0xFFFE5C3C, 0xFFFFE8A4, 0x25F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_A14)
    Sleep(300)

    def lambda_A34():
        OP_8E(0xFE, 0xFFFE5B4C, 0xFFFFE890, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_A34)
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x14F, 0x1)
    WaitChrThread(0x15, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #11
        "\x07\x05Mary picked up a \x07\x02gold chain\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_82(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #12
        0x14E,
        (
            "#1900FOh, so that's what it was! Well, it's certainly\x01",
            "counts as romantic...\x02\x03",

            "...but I'm not sure a chain alone is going to\x01",
            "make much of a present. We'll need a little\x01",
            "more than that.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_B80():
        TurnDirection(0xFE, 0x14F, 400)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_B80)
    Sleep(300)
    TurnDirection(0x14F, 0x14E, 300)
    Sleep(300)
    OP_8F(0x14E, 0xFFFE5B7E, 0xFFFFE89A, 0x2850, 0x3E8, 0x0)
    Sleep(400)

    ChrTalk(    #13
        0x14E,
        (
            "#1719F#6PYou can have it if you want. You were the\x01",
            "one who found it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x14E, 0xFFFE5C3C, 0xFFFFE8A4, 0x25F8, 0x3E8, 0x0)

    ChrTalk(    #14
        0x14E,
        (
            "#1710FIt might not be fitting for a present,\x01",
            "but it's still pretty.\x02\x03",

            "Take good care of it, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14F,
        (
            "#1730F...\x02\x03",

            "#1732FOkay!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    OP_62(0x14F, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(500)
    OP_8C(0x14F, 50, 400)
    Sleep(500)

    ChrTalk(    #16
        0x14F,
        "#1733FOh!\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(500)
    OP_8C(0x14E, 50, 400)

    def lambda_CF2():
        OP_6D(-106240, -5480, 19200, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_CF2)

    def lambda_D0A():
        OP_67(0, 7200, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_D0A)

    def lambda_D22():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_D22)

    def lambda_D32():
        OP_6C(306000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_D32)

    def lambda_D42():
        OP_6E(362, 4000)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_D42)
    WaitChrThread(0x15, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, -94410, -2000, 19980, 270)
    SetChrPos(0x11, -93280, -2000, 21020, 270)

    def lambda_D8D():
        OP_8E(0xFE, 0xFFFE69AC, 0xFFFFF830, 0x4F4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D8D)
    Sleep(100)

    def lambda_DAD():
        OP_8E(0xFE, 0xFFFE6EC0, 0xFFFFF830, 0x52BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_DAD)
    Sleep(2000)

    def lambda_DCD():
        OP_8E(0xFE, 0xFFFE6380, 0xFFFFE890, 0x33F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_DCD)

    def lambda_DE8():
        OP_8E(0xFE, 0xFFFE69FC, 0xFFFFE8CC, 0x3084, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_DE8)
    WaitChrThread(0x14F, 0x1)
    OP_8C(0x14F, 340, 400)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 340, 400)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #17
        0x14F,
        "#1732F#3S#2PIt's Lucia!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(100)
    OP_8C(0x11, 180, 400)
    Sleep(500)

    ChrTalk(    #18
        0x10,
        "Oh, Polly! Mary!\x02",
    )

    CloseMessageWindow()

    def lambda_E6B():
        OP_6D(-106000, -5580, 18700, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_E6B)

    def lambda_E83():
        OP_6B(2500, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E83)

    def lambda_E93():
        OP_67(0, 6300, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_E93)

    def lambda_EAB():
        OP_8E(0xFE, 0xFFFE69C0, 0xFFFFF808, 0x4AB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_EAB)
    Sleep(100)

    def lambda_ECB():
        OP_8F(0xFE, 0xFFFE6448, 0xFFFFE890, 0x3520, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_ECB)

    def lambda_EE6():
        OP_8F(0xFE, 0xFFFE6AC4, 0xFFFFE8CC, 0x31B0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_EE6)
    Sleep(200)

    def lambda_F06():
        OP_8E(0xFE, 0xFFFE6E98, 0xFFFFF830, 0x4C54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F06)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x11, 0x1)

    NpcTalk(    #19
        0x11,
        "Man",
        "#6PHeya, kids! Having fun playing on the beach?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x14E,
        (
            "#1714FY-Yes, that's right! We were trying to find\x01",
            "some nice shells, actually.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #21
        0x11,
        "Man",
        "#6PShells, huh?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #22
        0x11,
        "Man",
        (
            "#6PWell, take care, all right? I'm not gonna tell\x01",
            "you not to play here, but you just keep your\x01",
            "eyes peeled for monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14E,
        (
            "#1710FWe will. Fortunately, there don't seem to be\x01",
            "any here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x14F,
        "#1730F#5PYou going somewhere, Lucia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        "#6PWell, I was!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#6PYou know about the bazaar starting today in\x01",
            "Manoria, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        "#6PWe went to put up some posters for it in Ruan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x14E,
        "#1714FYou just reminded me of it, in fact.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x14F,
        "#1732F#5PI wanna gooo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "#6PYou should totally go, then!\x02\x03",

            "It'll be reeeally fun. Trust me! ★\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11EA():
        OP_8E(0xFE, 0xFFFE6C40, 0xFFFFF830, 0x4BB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_11EA)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #31
        0x10,
        "#6POkay! Let's get a move on!\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x2, 0x0, 0x6)
    Sleep(500)

    def lambda_123E():

        label("loc_123E")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_123E")

    QueueWorkItem2(0x14F, 2, lambda_123E)

    NpcTalk(    #32 op#A
        0x11,
        "Man",
        "#6P#20AH-Hey! Don't tug on my arm like that!\x02",
    )

    Sleep(2000)
    OP_56(0x0)
    WaitChrThread(0x10, 0x2)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x14F, 0x2)
    OP_44(0x14E, 0x2)

    def lambda_12A2():
        OP_6D(-104740, -6020, 14260, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_12A2)

    def lambda_12BA():
        OP_67(0, 7200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_12BA)

    def lambda_12D2():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_12D2)

    def lambda_12E2():
        OP_6C(336000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_12E2)

    def lambda_12F2():
        OP_6E(288, 3000)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_12F2)
    WaitChrThread(0x15, 0x0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1600)
    OP_63(0x14E)

    ChrTalk(    #33
        0x14E,
        (
            "#1714F(Wasn't he one of those bracers who helped\x01",
            "us before?)\x02\x03",

            "#1712F(I can't remember his name, though...)\x02\x03",

            "#1900F(There was Carna, Anelace...umm...Kurt...\x01",
            "then him...)\x02\x03",

            "(...What WAS his name...?)\x02",
        )
    )

    Sleep(1000)

    def lambda_13EF():
        TurnDirection(0xFE, 0x14E, 400)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_13EF)
    CloseMessageWindow()

    ChrTalk(    #34
        0x14F,
        "#1732F#1PMary? Maryyy!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14E, 0x14F, 400)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #35
        0x14E,
        "#1714FO-Oh... Sorry, Polly. What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x14F,
        "#1731F#1PI wanna go to the bazaar!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x14E,
        (
            "#1714F...The bazaar?\x02\x03",

            "#1718FOh, right. Sorry.\x02\x03",

            "#1900FWell, we might find something that works\x01",
            "as a present there if we do...\x02\x03",

            "#1710FOkay! Let's go see if we find something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14F,
        "#1732F#1PYay!\x02",
    )

    CloseMessageWindow()

    def lambda_154D():

        label("loc_154D")

        TurnDirection(0xFE, 0x14F, 0)
        OP_48()
        Jump("loc_154D")

    QueueWorkItem2(0x14E, 2, lambda_154D)

    def lambda_155E():
        OP_8E(0xFE, 0xFFFE712C, 0xFFFFE854, 0x3430, 0x1068, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_155E)
    Sleep(400)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #39
        0x14E,
        "#1717F#3PW-Wait a second!\x02",
    )

    CloseMessageWindow()
    OP_44(0x14E, 0x2)

    def lambda_15B3():
        OP_6D(-102480, -6020, 13720, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_15B3)

    def lambda_15CB():
        OP_6C(320000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_15CB)

    def lambda_15DB():

        label("loc_15DB")

        TurnDirection(0xFE, 0x14E, 0)
        OP_48()
        Jump("loc_15DB")

    QueueWorkItem2(0x14F, 2, lambda_15DB)

    def lambda_15EC():
        OP_8E(0xFE, 0xFFFE70C8, 0xFFFFE868, 0x31EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_15EC)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 60, 400)
    Sleep(500)
    OP_44(0x14F, 0x2)

    ChrTalk(    #40
        0x14E,
        (
            "#1716FIt's not safe to go running off on your own,\x01",
            "Polly!\x02\x03",

            "#1710FLet's go together, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x14F,
        "#1732F#4POkaaay.\x02",
    )

    CloseMessageWindow()

    def lambda_1691():
        OP_8E(0xFE, 0xFFFE717C, 0xFFFFE868, 0x3228, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1691)
    WaitChrThread(0x14E, 0x1)

    def lambda_16B1():
        OP_8E(0xFE, 0xFFFE988C, 0xFFFFE854, 0x3228, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_16B1)

    def lambda_16CC():
        OP_8E(0xFE, 0xFFFE983C, 0xFFFFE854, 0x3430, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_16CC)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-88980, -5920, 11820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x14E, 0xFF)
    OP_44(0x14F, 0xFF)
    SetChrPos(0x14E, -88980, -5920, 11820, 0)
    SetChrPos(0x14F, -88980, -5920, 11820, 0)
    SetChrChipByIndex(0x14E, 65535)
    SetChrSubChip(0x14E, 0)
    SetChrChipByIndex(0x14F, 65535)
    SetChrSubChip(0x14F, 0)
    ClearChrFlags(0x14E, 0x40)
    OP_69(0x14E, 0x0)
    OP_A2(0x2F20)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_3_52B end

    def Function_4_1791(): pass

    label("Function_4_1791")

    Sleep(1500)
    OP_8C(0x14E, 200, 400)
    Sleep(1000)
    OP_8C(0x14E, 90, 400)
    Sleep(500)

    def lambda_17B4():
        OP_8E(0xFE, 0xFFFE6A60, 0xFFFFE8E0, 0x2DDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_17B4)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 50, 400)
    Sleep(800)
    OP_8C(0x14E, 130, 400)
    Sleep(1000)

    def lambda_17F1():
        OP_8E(0xFE, 0xFFFE63E4, 0xFFFFE8A4, 0x29CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_17F1)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 120, 400)
    Sleep(1000)
    OP_8C(0x14E, 180, 400)
    Sleep(1000)
    Return()

    # Function_4_1791 end

    def Function_5_1829(): pass

    label("Function_5_1829")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1841")
    TurnDirection(0xFE, 0x14E, 100)
    Sleep(100)
    Jump("Function_5_1829")

    label("loc_1841")

    Return()

    # Function_5_1829 end

    def Function_6_1842(): pass

    label("Function_6_1842")


    def lambda_1848():
        OP_8F(0xFE, 0xFFFE6858, 0xFFFFF830, 0x4BB4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1848)

    def lambda_1863():
        OP_8F(0xFE, 0xFFFE6AB0, 0xFFFFF830, 0x4C54, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1863)
    WaitChrThread(0x10, 0x1)
    Sleep(600)

    def lambda_1888():
        OP_8F(0xFE, 0xFFFE6470, 0xFFFFF830, 0x4BB4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1888)

    def lambda_18A3():
        OP_8F(0xFE, 0xFFFE66C8, 0xFFFFF830, 0x4C54, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_18A3)
    WaitChrThread(0x10, 0x1)
    Sleep(600)

    def lambda_18C8():
        OP_8F(0xFE, 0xFFFE6088, 0xFFFFF830, 0x4BB4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_18C8)

    def lambda_18E3():
        OP_8F(0xFE, 0xFFFE62E0, 0xFFFFF830, 0x4C54, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_18E3)
    WaitChrThread(0x10, 0x1)
    Sleep(600)

    def lambda_1908():
        OP_8F(0xFE, 0xFFFE4968, 0xFFFFF830, 0x4BB4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1908)

    def lambda_1923():
        OP_8F(0xFE, 0xFFFE4B70, 0xFFFFF830, 0x4C54, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1923)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_6_1842 end

    def Function_7_193E(): pass

    label("Function_7_193E")

    SetMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 2)), scpexpr(EXPR_END)), "loc_19B2")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x05Much to Mary and Polly's dismay, this chest is empty as can be.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1D50")

    label("loc_19B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_1BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A56")
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #43
        0x14E,
        (
            "#1714FWhat's a treasure chest doing here?\x02\x03",

            "I-I wonder what's inside it...\x02\x03",

            "#1712FMaybe Polly's hiding inside?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F45)

    label("loc_1A56")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Open\x01",            # 0
            "Don't Open\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9A")

    ChrTalk(    #44
        0x14E,
        (
            "#1715FL-Let's see what's in here...\x01",
            "*gulp*\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05The poor chest was empty-umpty-dumpty.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #46
        0x14E,
        "#1714F...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #47
        0x14E,
        "#1717F#4SAaargh! If it's empty, who closed it?!#2S\x02",
    )

    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_A2(0x2F1A)
    Jump("loc_1BDF")

    label("loc_1B9A")


    ChrTalk(    #48
        0x14E,
        (
            "#1713FNo. I mustn't...but I really want to know\x01",
            "what's in it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDF")

    Jump("loc_1D50")

    label("loc_1BE2")

    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #49
        0x14E,
        "#1714FO-Oh! Isn't this...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14F,
        "#1732FIt's a treasure chest!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x14E,
        (
            "#1712FD-Do you want to see what's inside?\x01",
            "Okay, three, two, one...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        "\x07\x05Much to Mary and Polly's dismay, this chest is empty as can be.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_7C(0xC8, 0x96, 0xBB8, 0x1F4)

    ChrTalk(    #53
        0x14E,
        "#1717F#4SNoooooo!\x02",
    )


    ChrTalk(    #54
        0x14F,
        "#1733F#4SNooooooooo!\x02",
    )

    OP_56(0x1)
    Sleep(1000)
    OP_59()
    OP_A2(0x2F1A)

    label("loc_1D50")

    ClearMapFlags(0x20)
    TalkEnd(0xFF)
    Return()

    # Function_7_193E end

    def Function_8_1D59(): pass

    label("Function_8_1D59")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05Mary looked in the sand for seashells.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #56
        0x14E,
        "#1713FAww... I can't see any pretty ones around here.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F1B)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1E")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_1E1E")

    TalkEnd(0xFF)
    Return()

    # Function_8_1D59 end

    def Function_9_1E22(): pass

    label("Function_9_1E22")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #57
        "\x07\x05Mary looked in the sand for seashells.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #58
        0x14E,
        (
            "#1718FOooh! A pretty pink one!\x02\x03",

            "#1716F...It's cracked. What a shame...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F1C)
    OP_64(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF8")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_1EF8")

    TalkEnd(0xFF)
    Return()

    # Function_9_1E22 end

    def Function_10_1EFC(): pass

    label("Function_10_1EFC")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05Mary looked in the sand for seashells.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #60
        0x14E,
        (
            "#1712FI can't see any nice-looking ones around here...\x02\x03",

            "#1900F...\x02\x03",

            "#1716FHow nice it'd be to bump into a happiness stone...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F1D)
    OP_64(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2007")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2007")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_2007")

    TalkEnd(0xFF)
    Return()

    # Function_10_1EFC end

    def Function_11_200B(): pass

    label("Function_11_200B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x05Mary looked in the sand for seashells.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #62
        0x14E,
        (
            "#1716F*sigh* Nope. Nothing but garbage here...\x02\x03",

            "#1715FWhat kind of terrible person would throw\x01",
            "a used cigarette on the beach? Adults can\x01",
            "be so awful sometimes!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F1E)
    OP_64(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_213A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213A")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_213A")

    TalkEnd(0xFF)
    Return()

    # Function_11_200B end

    def Function_12_213E(): pass

    label("Function_12_213E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #63
        "\x07\x05Mary looked in the sand for seashells.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #64
        0x14E,
        (
            "#1710FThis one feels kind of nice in the hand,\x01",
            "but I'm not very fond of the color.\x02\x03",

            "#1900FI prefer one a little lighter...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F1F)
    OP_64(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2248")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2248")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_2248")

    TalkEnd(0xFF)
    Return()

    # Function_12_213E end

    def Function_13_224C(): pass

    label("Function_13_224C")

    OP_8B(0x14F, 0xFFFF2ACC, 0x3624, 0x190)
    Sleep(500)

    ChrTalk(    #65
        0x14F,
        (
            "#1733FWhat about these, Mary?\x02\x03",

            "#1732FWouldn't these make a good present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x14E,
        (
            "#1714FHmm...\x02\x03",

            "#1710FWell, they're certainly pretty, but we've got \x01",
            "plenty of flowers growing in our garden as it\x01",
            "is.\x02\x03",

            "I'd like to get the matron something a little\x01",
            "more special and unusual.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F18)
    OP_64(0x8, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_13_224C end

    def Function_14_237A(): pass

    label("Function_14_237A")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_242D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_23EF")

    ChrTalk(    #67
        0x14E,
        (
            "#1713FI need to get back to searching for Polly...\x02\x03",

            "It's my fault she got lost, after all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242A")

    label("loc_23EF")


    ChrTalk(    #68
        0x14E,
        "#1713FI don't think Polly will have come this way.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_242A")

    Jump("loc_25E3")

    label("loc_242D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_24AE")

    ChrTalk(    #69
        0x14E,
        (
            "#1710FThis isn't the way to the Krone mountains.\x02\x03",

            "#1711FI need to head north from Manoria Village\x01",
            "to get to them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_24AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_2539")

    ChrTalk(    #70
        0x14E,
        (
            "#1714FWait. This is the path that leads to Ruan...\x02\x03",

            "#1710FWhat am I thinking? Manoria Village is in the\x01",
            "opposite direction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_2539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_25E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2581")

    ChrTalk(    #71
        0x14E,
        "#1710FThe beach is on the way to Manoria Village.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_2581")


    ChrTalk(    #72
        0x14E,
        (
            "#1714FWait. This is the path that leads to Ruan...\x02\x03",

            "#1710FWe shouldn't be going this way.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_25E3")

    OP_59()
    Fade(1000)
    SetChrPos(0x14E, -5800, -2000, 30000, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4E)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2619")
    SetChrPos(0x14F, -5800, -2000, 30000, 270)

    label("loc_2619")

    OP_6D(-7800, -2000, 30000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_14_237A end

    def Function_15_2633(): pass

    label("Function_15_2633")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2691")

    ChrTalk(    #73
        0x14E,
        (
            "#1710FThis way leads to Manoria Village. We need to\x01",
            "retrace our steps a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26F0")

    label("loc_2691")


    ChrTalk(    #74
        0x14E,
        (
            "#1714FOops. I think we've gone past the beach.\x01",
            "This is the path that leads to Manoria.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_26F0")

    OP_59()
    Fade(1000)
    SetChrPos(0x14E, -123000, -2060, 15120, 90)
    SetChrPos(0x14F, -123000, -2060, 15120, 90)
    OP_6D(-122820, -2060, 15120, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_15_2633 end

    def Function_16_2732(): pass

    label("Function_16_2732")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #75
        "\x07\x05North: Mercia Orphanage\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_2732 end

    def Function_17_277C(): pass

    label("Function_17_277C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27F3")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #76
        (
            "\x07\x05East: Ruan - 238 selge\x01",
            "West: Manoria Village - 74 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Jump("loc_29AD")

    label("loc_27F3")


    ChrTalk(    #77
        0x14F,
        "#1733FWhat's this, Mary?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x14E,
        (
            "#1710FIt's a sign that says 'Ruan' on it.\x02\x03",

            "It's saying that if we follow this road straight,\x01",
            "we'll end up in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x14F,
        "#1731F...Present.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14E, 0x14F, 400)
    Sleep(300)

    ChrTalk(    #80
        0x14E,
        (
            "#1714FWhat?\x02\x03",

            "You're not suggesting giving this sign to the\x01",
            "matron as a present, are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    Sleep(1500)

    ChrTalk(    #81
        0x14E,
        (
            "#1712FNow you're just being silly!\x02\x03",

            "We're trying to choose a present seriously here,\x01",
            "not pull some kind of prank like Clem does!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F19)
    TalkEnd(0xFF)

    label("loc_29AD")

    Return()

    # Function_17_277C end

    SaveToFile()

Try(main)
