from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U5111   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U5111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Plate',                                # 9
        'Plate',                                # 10
        'Plate',                                # 11
        'Bottle',                               # 12
        'Bottle',                               # 13
        'Fork',                                 # 14
        'Knife',                                # 15
        'Empty Glass',                          # 16
        'Gilbert',                              # 17
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
        'ED6_DT06/CH20020 ._CH',             # 00
        'ED6_DT06/CH20021 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT06/CH20020P._CP',             # 00
        'ED6_DT06/CH20021P._CP',             # 01
    )

    DeclNpc(
        X                   = 18160,
        Z                   = 800,
        Y                   = 11100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18670,
        Z                   = 800,
        Y                   = 12140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18200,
        Z                   = 800,
        Y                   = 11940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17600,
        Z                   = 800,
        Y                   = 12140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835008,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17900,
        Z                   = 800,
        Y                   = 11800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835008,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17600,
        Z                   = 800,
        Y                   = 11180,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917504,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18470,
        Z                   = 800,
        Y                   = 11100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 851968,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18350,
        Z                   = 800,
        Y                   = 11550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65537,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 112940,
        Z                   = 0,
        Y                   = -3200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 112600,
        Y                   = 0,
        Z                   = 1000,
        Range               = 115170,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = 21010,
        TriggerZ            = 0,
        TriggerY            = 15470,
        TriggerRange        = 1000,
        ActorX              = 21010,
        ActorZ              = 2000,
        ActorY              = 15470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 86740,
        TriggerZ            = 0,
        TriggerY            = 41680,
        TriggerRange        = 1000,
        ActorX              = 86740,
        ActorZ              = 1000,
        ActorY              = 41680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 139740,
        TriggerZ            = 0,
        TriggerY            = 41770,
        TriggerRange        = 1000,
        ActorX              = 139740,
        ActorZ              = 1000,
        ActorY              = 41770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 115250,
        TriggerZ            = 0,
        TriggerY            = -34470,
        TriggerRange        = 1000,
        ActorX              = 115250,
        ActorZ              = 1000,
        ActorY              = -34470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 142700,
        TriggerZ            = 0,
        TriggerY            = -34000,
        TriggerRange        = 1000,
        ActorX              = 142700,
        ActorZ              = 1000,
        ActorY              = -34000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_314",          # 01, 1
        "Function_2_38A",          # 02, 2
        "Function_3_4A4",          # 03, 3
        "Function_4_5E2",          # 04, 4
        "Function_5_732",          # 05, 5
        "Function_6_851",          # 06, 6
        "Function_7_DCF",          # 07, 7
        "Function_8_1051",         # 08, 8
        "Function_9_12D5",         # 09, 9
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CF")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_2CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_313")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_313")

    Return()

    # Function_0_2AE end

    def Function_1_314(): pass

    label("Function_1_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_325")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337")
    OP_6F(0x1D, 0)
    Jump("loc_33E")

    label("loc_337")

    OP_6F(0x1D, 60)

    label("loc_33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350")
    OP_6F(0x1E, 0)
    Jump("loc_357")

    label("loc_350")

    OP_6F(0x1E, 60)

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369")
    OP_6F(0x1F, 0)
    Jump("loc_370")

    label("loc_369")

    OP_6F(0x1F, 60)

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382")
    OP_6F(0x20, 0)
    Jump("loc_389")

    label("loc_382")

    OP_6F(0x20, 60)

    label("loc_389")

    Return()

    # Function_1_314 end

    def Function_2_38A(): pass

    label("Function_2_38A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D9, 1)"), scpexpr(EXPR_END)), "loc_3F8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xD9\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2998)
    Jump("loc_460")

    label("loc_3F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xD9\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xD9\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_460")

    Jump("loc_496")

    label("loc_463")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Chest in peace.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x145, 0x0)

    label("loc_496")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_38A end

    def Function_3_4A4(): pass

    label("Function_3_4A4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29C, 1)"), scpexpr(EXPR_END)), "loc_512")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x9C\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2999)
    Jump("loc_57A")

    label("loc_512")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x9C\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x9C\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_57A")

    Jump("loc_5D4")

    label("loc_57D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05It costs money to open me more than once, you know.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x146, 0x0)

    label("loc_5D4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4A4 end

    def Function_4_5E2(): pass

    label("Function_4_5E2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18C, 1)"), scpexpr(EXPR_END)), "loc_650")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x8C\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x299A)
    Jump("loc_6B8")

    label("loc_650")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x8C\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x8C\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_6B8")

    Jump("loc_724")

    label("loc_6BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Hey. You. I've got some good stuff under my lid. Are you...inchested?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x147, 0x0)

    label("loc_724")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5E2 end

    def Function_5_732(): pass

    label("Function_5_732")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x533, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_810")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x1E)
    OP_73(0x20)
    OP_6F(0x20, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1EC, 1)

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\xEC\x01\x07\x05.\x02",
    )

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x28)"), scpexpr(EXPR_END)), "loc_79D")
    Jump("loc_7FE")

    label("loc_79D")

    CloseMessageWindow()

    AnonymousTalk(    #10
        "\x07\x05Found a scrap of paper with a recipe written on it.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #11
        "\x07\x05Learned the recipe for \x1F\xEC\x01\x07\x05.\x02",
    )


    label("loc_7FE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x299B)
    Jump("loc_83A")

    label("loc_810")


    AnonymousTalk(    #12
        "\x07\x05I tried. (This is a chest phrase.)\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_83A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x148, 0x0)
    Return()

    # Function_5_732 end

    def Function_6_851(): pass

    label("Function_6_851")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 21630, 0, 12910, 180)
    SetChrPos(0x102, 20700, 0, 13000, 180)
    SetChrPos(0xF0, 20520, 0, 14070, 180)
    SetChrPos(0xF1, 21540, 0, 13940, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(22000, 0, 14800, 0)
    OP_67(0, 6660, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_910():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_910)
    FadeToBright(2000, 0)
    Sleep(1000)
    LoadEffect(0x0, "map\\mp252_04.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(2000)

    def lambda_A24():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A24)

    def lambda_A36():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A36)

    def lambda_A48():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A48)

    def lambda_A5A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A5A)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    OP_83(0x0, 0x2)
    OP_83(0x1, 0x2)
    OP_83(0x2, 0x2)
    OP_83(0x3, 0x2)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEB")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B52")

    label("loc_AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B13")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B52")

    label("loc_B13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B52")

    label("loc_B3B")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B52")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BE6")

    label("loc_B7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BE6")

    label("loc_BA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BE6")

    label("loc_BCF")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BE6")

    Sleep(1200)

    def lambda_BF1():
        OP_6D(24480, 0, 14710, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BF1)

    def lambda_C09():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C09)
    Sleep(100)

    def lambda_C1C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C1C)
    Sleep(100)

    def lambda_C2F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_C2F)
    Sleep(100)

    def lambda_C42():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_C42)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #13
        0x109,
        "#1079F#6PHold on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#1504F#6PThat light wasn't on when we were last here.\x02\x03",

            "#1503FIt's dark outside now, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1065F#6PYeah... It's night here now, just like how the\x01",
            "time of day changed on the second plane.\x02\x03",

            "#1063FAnd I'd wager the time of day isn't the only\x01",
            "thing that's changed here. Let's see if we can\x01",
            "find anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1502F#6PGot it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x290F)
    OP_28(0x34, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_6_851 end

    def Function_7_DCF(): pass

    label("Function_7_DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9E")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(2816)
    Sleep(500)
    Jump("loc_EA1")

    label("loc_E9E")

    TalkBegin(0xFF)

    label("loc_EA1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1020")

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
        (0, "loc_F39"),
        (1, "loc_FB4"),
        (2, "loc_FE2"),
        (SWITCH_DEFAULT, "loc_1010"),
    )


    label("loc_F39")

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
    OP_1D(0xDD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_101D")

    label("loc_FB4")

    OP_A9(0x1E)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_101D")

    label("loc_FE2")

    OP_A9(0x6)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_101D")

    label("loc_1010")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_101D")

    label("loc_101D")

    Jump("loc_EDD")

    label("loc_1020")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104D")
    OP_A2(0x258E)
    EventEnd(0x1)
    Jump("loc_1050")

    label("loc_104D")

    TalkEnd(0xFF)

    label("loc_1050")

    Return()

    # Function_7_DCF end

    def Function_8_1051(): pass

    label("Function_8_1051")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1061")
    Return()

    label("loc_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106A")
    Return()

    label("loc_106A")

    EventBegin(0x1)
    OP_8C(0x0, 174, 500)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125D")
    OP_A2(0x0)

    NpcTalk(    #20
        0x18,
        "Gilbert's Voice",
        (
            "#5P#40W*chomp* *chomp* *chomp*\x01",
            "Hmph... *munch* *munch*\x02\x03",

            "Why would I...*munch*...ever want\x01",
            "to be helped by THEM? *munch*\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x18, 0x1, 0x0, 0x9)

    NpcTalk(    #21
        0x18,
        "Gilbert's Voice",
        (
            "#5P#60WGuh!#500W \x01",
            "#40WGraaaaaah!#500W\x01",
            "#20W*sound of banging on chest*\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #22
        0x18,
        "Gilbert's Voice",
        "#5P#4SAaaaaah!\x02",
    )

    OP_7C(0x12C, 0x12C, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #23
        0x18,
        "Gilbert's Voice",
        "#5P#40WI-I thought I was gonna die...\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    NpcTalk(    #24
        0x18,
        "Gilbert's Voice",
        (
            "#5P#40W...Huh? What's this?\x01",
            "Sweat's coming from my eyes...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B9")

    label("loc_125D")


    NpcTalk(    #25
        0x18,
        "Gilbert's Voice",
        (
            "#5P#40WI'm not crying! I'm not...\x02\x03",

            "*sniffle* *munch*\x01",
            "*sniffle* *scarf*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B9")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_8_1051 end

    def Function_9_12D5(): pass

    label("Function_9_12D5")

    OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
    Sleep(800)
    OP_7C(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    OP_22(0x72, 0x0, 0x64)
    Return()

    # Function_9_12D5 end

    SaveToFile()

Try(main)
