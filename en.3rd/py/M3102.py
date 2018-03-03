from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M3102   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3102.x',
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
        'Airship',                              # 9
        "Airship's Shadow",                     # 10
        'Searchlight',                          # 11
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 9240,
        TriggerZ            = 0,
        TriggerY            = 18600,
        TriggerRange        = 1000,
        ActorX              = 9430,
        ActorZ              = 1000,
        ActorY              = 18590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1450,
        TriggerZ            = 0,
        TriggerY            = 45310,
        TriggerRange        = 1000,
        ActorX              = -1450,
        ActorZ              = 1000,
        ActorY              = 45510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_17E",          # 01, 1
        "Function_2_1B1",          # 02, 2
        "Function_3_2D8",          # 03, 3
        "Function_4_42D",          # 04, 4
        "Function_5_147B",         # 05, 5
        "Function_6_17EC",         # 06, 6
        "Function_7_183A",         # 07, 7
        "Function_8_1A5D",         # 08, 8
        "Function_9_1C68",         # 09, 9
        "Function_10_1DE6",        # 0A, 10
        "Function_11_209C",        # 0B, 11
        "Function_12_2356",        # 0C, 12
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_168")
    Jump("loc_17D")

    label("loc_168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_17D")

    Return()

    # Function_0_152 end

    def Function_1_17E(): pass

    label("Function_1_17E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190")
    OP_6F(0x11, 0)
    Jump("loc_197")

    label("loc_190")

    OP_6F(0x11, 60)

    label("loc_197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9")
    OP_6F(0x12, 0)
    Jump("loc_1B0")

    label("loc_1A9")

    OP_6F(0x12, 60)

    label("loc_1B0")

    Return()

    # Function_1_17E end

    def Function_2_1B1(): pass

    label("Function_2_1B1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x148, 1)"), scpexpr(EXPR_END)), "loc_21F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x48\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BFD)
    Jump("loc_287")

    label("loc_21F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x48\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x48\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_287")

    Jump("loc_2CA")

    label("loc_28A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05I'm telling my mommy on you!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x1A, 0x0)

    label("loc_2CA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1B1 end

    def Function_3_2D8(): pass

    label("Function_3_2D8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x149, 1)"), scpexpr(EXPR_END)), "loc_346")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x49\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BFE)
    Jump("loc_3AE")

    label("loc_346")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x49\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x49\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_3AE")

    Jump("loc_41F")

    label("loc_3B1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05They say it's what's on the inside that counts. Now look what you've\x01",
            "done.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x1B, 0x0)

    label("loc_41F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2D8 end

    def Function_4_42D(): pass

    label("Function_4_42D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp078_00.eff")
    LoadEffect(0x1, "map\\mp003_00.eff")
    LoadEffect(0x2, "map\\mp280_00.eff")
    LoadEffect(0x3, "map\\mp301_00.eff")
    OP_E0(238, 0x40, 0x2)
    OP_E0(238, 0x41, 0x3)
    OP_E0(238, 0x42, 0x4)
    OP_E0(239, 0x43, 0x2)
    OP_E0(239, 0x44, 0x3)
    OP_E0(239, 0x45, 0x4)
    OP_E0(240, 0x46, 0x2)
    OP_E0(240, 0x47, 0x3)
    OP_E0(240, 0x48, 0x4)
    OP_E0(241, 0x49, 0x2)
    OP_E0(241, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 98690, 30000, 32540, 60)
    OP_A1(0x10, 0x0)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 1000)
    OP_70(0x0, 0x3E8)
    PlayEffect(0x3, 0x6, 0xFF, 96000, 30000, 31000, 50, -70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 2390, 100, 22000, 90)
    OP_A1(0x11, 0x10)
    OP_71(0x410, 0x0)
    ExitThread()
    SetChrPos(0x109, -18450, 0, 20650, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59F")
    SetChrPos(0xEF, -18850, 0, 22010, 90)
    SetChrPos(0xF0, -20210, 0, 20210, 90)
    SetChrPos(0xF1, -20500, 0, 21990, 90)
    Jump("loc_624")

    label("loc_59F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E3")
    SetChrPos(0xF0, -18850, 0, 22010, 90)
    SetChrPos(0xEF, -20210, 0, 20210, 90)
    SetChrPos(0xF1, -20500, 0, 21990, 90)
    Jump("loc_624")

    label("loc_5E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_624")
    SetChrPos(0xF1, -18850, 0, 22010, 90)
    SetChrPos(0xEF, -20210, 0, 20210, 90)
    SetChrPos(0xF0, -20500, 0, 21990, 90)

    label("loc_624")

    StopSound(0x9470, 0x30D40, 0x0)
    OP_6D(5310, 0, 22200, 0)
    OP_67(0, 7910, -10000, 0)
    OP_6B(6180, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)

    def lambda_674():
        OP_6D(-5220, 0, 23370, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_674)

    def lambda_68C():
        OP_8F(0xFE, 0xFFFFE4BC, 0x0, 0x4F42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_68C)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712")

    def lambda_6BA():
        OP_8F(0xFE, 0xFFFFE516, 0x0, 0x5564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_6BA)
    Sleep(100)

    def lambda_6DA():
        OP_8F(0xFE, 0xFFFFDE40, 0x0, 0x4DDA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6DA)
    Sleep(100)

    def lambda_6FA():
        OP_8F(0xFE, 0xFFFFDDD2, 0x0, 0x54BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_6FA)
    Jump("loc_7E7")

    label("loc_712")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77E")

    def lambda_726():
        OP_8F(0xFE, 0xFFFFE516, 0x0, 0x5564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_726)
    Sleep(100)

    def lambda_746():
        OP_8F(0xFE, 0xFFFFDE40, 0x0, 0x4DDA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_746)
    Sleep(100)

    def lambda_766():
        OP_8F(0xFE, 0xFFFFDDD2, 0x0, 0x54BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_766)
    Jump("loc_7E7")

    label("loc_77E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E7")

    def lambda_792():
        OP_8F(0xFE, 0xFFFFE516, 0x0, 0x5564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_792)
    Sleep(100)

    def lambda_7B2():
        OP_8F(0xFE, 0xFFFFDE40, 0x0, 0x4DDA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_7B2)
    Sleep(100)

    def lambda_7D2():
        OP_8F(0xFE, 0xFFFFDDD2, 0x0, 0x54BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_7D2)

    label("loc_7E7")

    FadeToBright(2000, 0)
    WaitChrThread(0xEE, 0x3)
    Fade(500)
    StopSound(0x9470, 0x1FBD0, 0x0)
    ClearMapFlags(0x10)
    OP_6D(-6500, 0, 22060, 0)
    OP_67(0, 6910, -10000, 0)
    OP_6B(3390, 0)
    OP_6C(45000, 0)
    OP_6E(220, 0)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x10C,
        "#112F#5PWait...\x02",
    )

    CloseMessageWindow()
    OP_22(0x79, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EA")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_951")

    label("loc_8EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_912")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_951")

    label("loc_912")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93A")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_951")

    label("loc_93A")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_951")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9E5")

    label("loc_97E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A6")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9E5")

    label("loc_9A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CE")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9E5")

    label("loc_9CE")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9E5")

    Sleep(1000)
    Jump("loc_C5C")

    label("loc_9ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B26")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A23")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A8A")

    label("loc_A23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4B")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A8A")

    label("loc_A4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A73")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A8A")

    label("loc_A73")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A8A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB7")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B1E")

    label("loc_AB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B1E")

    label("loc_ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B07")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B1E")

    label("loc_B07")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B1E")

    Sleep(1000)
    Jump("loc_C5C")

    label("loc_B26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5C")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BC3")

    label("loc_B5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B84")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BC3")

    label("loc_B84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAC")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BC3")

    label("loc_BAC")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BC3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF0")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C57")

    label("loc_BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C18")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C57")

    label("loc_C18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C40")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C57")

    label("loc_C40")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C57")

    Sleep(1000)

    label("loc_C5C")


    ChrTalk(    #7
        0x109,
        "#1079F#6PTh-That sounds like...\x02",
    )

    CloseMessageWindow()
    OP_22(0x64, 0x0, 0x64)
    SetChrPos(0x12, -8000, 0, 21000, 90)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    PlayEffect(0x2, 0x7, 0x12, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_22(0x35A, 0x1, 0x64)
    Sleep(500)

    ChrTalk(    #8
        0x10C,
        "#114F#5P#3SEveryone, spread out!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_D31():
        OP_6D(-7100, 0, 22060, 500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_D31)

    def lambda_D49():
        OP_67(0, 6070, -10000, 500)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_D49)

    def lambda_D61():
        OP_6B(3100, 500)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_D61)

    def lambda_D71():
        OP_6E(243, 500)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_D71)
    OP_22(0x235, 0x0, 0x64)
    Sleep(70)
    OP_43(0xEE, 0x0, 0x0, 0x6)
    OP_43(0xEF, 0x0, 0x0, 0x7)
    Sleep(30)
    OP_43(0x10, 0x0, 0x0, 0x8)
    OP_43(0x10, 0x1, 0x0, 0x9)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xEE, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_23(0x35A)

    def lambda_DC7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_DC7)
    Sleep(100)

    def lambda_DDA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_DDA)
    Sleep(100)

    def lambda_DED():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_DED)
    Sleep(100)
    OP_8C(0xF1, 90, 400)
    Sleep(1000)
    Sleep(300)
    Fade(1000)
    OP_6D(95240, 30000, 29870, 0)
    OP_67(0, -9470, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(659, 0)
    OP_72(0x400, 0x0)
    ExitThread()

    def lambda_E59():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_E59)
    OP_22(0x35A, 0x1, 0x64)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 1000)
    OP_70(0x0, 0x3AD)
    OP_73(0x0)
    OP_23(0x35A)
    OP_6F(0x0, 940)
    OP_70(0x0, 0x385)
    OP_73(0x0)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 701)
    OP_70(0x0, 0x384)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE4")
    SetMessageWindowPos(200, 400, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #9
        "\x07\x00#1802FOh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_F14")

    label("loc_EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F14")
    SetMessageWindowPos(200, 400, -1, -1)
    SetChrName("Kloe")

    AnonymousTalk(    #10
        "\x07\x00#1164FOh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4D")
    SetMessageWindowPos(230, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #11
        "\x07\x00#1020FUh-oh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_F84")

    label("loc_F4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F84")
    SetMessageWindowPos(230, 400, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #12
        "\x07\x00#216FOh, boy...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBA")
    SetMessageWindowPos(180, 400, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #13
        "\x07\x00#1506FUgh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_FF1")

    label("loc_FBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF1")
    SetMessageWindowPos(180, 400, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #14
        "\x07\x00#1524FUgh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_FF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1022")
    SetMessageWindowPos(190, 400, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #15
        "\x07\x00#065FEeek...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1022")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1058")
    SetMessageWindowPos(220, 400, -1, -1)
    SetChrName("Anelace")

    AnonymousTalk(    #16
        "\x07\x00#1317FUh-oh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1058")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108C")
    SetMessageWindowPos(250, 400, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #17
        "\x07\x00#057FBah...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_10BF")

    label("loc_108C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BF")
    SetMessageWindowPos(250, 400, -1, -1)
    SetChrName("Mueller")

    AnonymousTalk(    #18
        "\x07\x00#271FGah...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_10BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F3")
    SetMessageWindowPos(210, 400, -1, -1)
    SetChrName("Julia")

    AnonymousTalk(    #19
        "\x07\x00#177FUgh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1122")

    label("loc_10F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1122")
    SetMessageWindowPos(210, 400, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #20
        "\x07\x00#077FUgh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1122")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115B")
    SetMessageWindowPos(170, 400, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #21
        "\x07\x00#1542FOh, dear...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_115B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1190")
    SetMessageWindowPos(240, 400, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #22
        "\x07\x00#1305FOh, my...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1190")

    Sleep(300)
    Fade(500)
    OP_6D(-4720, 0, 22090, 0)
    OP_67(0, 5670, -10000, 0)
    OP_6B(4059, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x410, 0x0)
    ExitThread()
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x109,
        "#1069F#5PGah... We don't stand a chance!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10C,
        (
            "#117F#5PIndeed! We have nothing to gain\x01",
            "by staying here any longer!\x02\x03",

            "Retreat!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_126A():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_126A)
    Sleep(100)

    def lambda_127D():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_127D)
    Sleep(100)

    def lambda_1290():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1290)
    Sleep(100)

    def lambda_12A3():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_12A3)
    Sleep(100)
    OP_22(0x35A, 0x1, 0x64)

    def lambda_12BB():
        OP_6D(-14870, 2300, 20910, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_12BB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1339")

    def lambda_12E1():
        OP_8F(0xFE, 0xFFFF8A8A, 0x190, 0x5D48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_12E1)
    Sleep(100)

    def lambda_1301():
        OP_8F(0xFE, 0xFFFF8C38, 0x190, 0x56D6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1301)
    Sleep(100)

    def lambda_1321():
        OP_8F(0xFE, 0xFFFF925A, 0x190, 0x5CE4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_1321)
    Jump("loc_140E")

    label("loc_1339")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A5")

    def lambda_134D():
        OP_8F(0xFE, 0xFFFF8A8A, 0x190, 0x5D48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_134D)
    Sleep(100)

    def lambda_136D():
        OP_8F(0xFE, 0xFFFF8C38, 0x190, 0x56D6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_136D)
    Sleep(100)

    def lambda_138D():
        OP_8F(0xFE, 0xFFFF925A, 0x190, 0x5CE4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_138D)
    Jump("loc_140E")

    label("loc_13A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140E")

    def lambda_13B9():
        OP_8F(0xFE, 0xFFFF8A8A, 0x190, 0x5D48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_13B9)
    Sleep(100)

    def lambda_13D9():
        OP_8F(0xFE, 0xFFFF8C38, 0x190, 0x56D6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_13D9)
    Sleep(100)

    def lambda_13F9():
        OP_8F(0xFE, 0xFFFF925A, 0x190, 0x5CE4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_13F9)

    label("loc_140E")


    def lambda_1414():
        OP_8F(0xFE, 0xFFFF934A, 0x190, 0x5708, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1414)
    Sleep(500)
    OP_43(0x11, 0x0, 0x0, 0x5)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0xC)
    Sleep(100)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x10, 0x1, 0x0, 0xB)
    OP_23(0x35A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x10)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M3101   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_4_42D end

    def Function_5_147B(): pass

    label("Function_5_147B")


    def lambda_1481():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1481)

    def lambda_149C():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_149C)
    Sleep(300)

    def lambda_14BC():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_14BC)

    def lambda_14D7():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_14D7)
    Sleep(300)

    def lambda_14F7():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_14F7)

    def lambda_1512():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1512)
    Sleep(300)

    def lambda_1532():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1532)

    def lambda_154D():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_154D)
    Sleep(200)

    def lambda_156D():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_156D)

    def lambda_1588():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1588)
    Sleep(200)

    def lambda_15A8():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_15A8)

    def lambda_15C3():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_15C3)
    Sleep(200)

    def lambda_15E3():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_15E3)

    def lambda_15FE():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_15FE)
    Sleep(100)

    def lambda_161E():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_161E)

    def lambda_1639():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1639)
    Sleep(100)

    def lambda_1659():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1659)

    def lambda_1674():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1674)
    Sleep(100)

    def lambda_1694():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1694)

    def lambda_16AF():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_16AF)
    Sleep(100)

    def lambda_16CF():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_16CF)

    def lambda_16EA():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_16EA)
    Sleep(100)

    def lambda_170A():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_170A)

    def lambda_1725():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1725)
    Sleep(100)

    def lambda_1745():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1745)

    def lambda_1760():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1760)
    Sleep(100)

    def lambda_1780():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1780)

    def lambda_179B():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_179B)
    Sleep(100)

    def lambda_17BB():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_17BB)

    def lambda_17D6():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_17D6)
    Return()

    # Function_5_147B end

    def Function_6_17EC(): pass

    label("Function_6_17EC")

    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 2)
    SetChrSubChip(0xEE, 0)
    OP_8C(0xFE, 45, 0)

    def lambda_1808():
        OP_96(0xFE, 0xFFFFE1E2, 0x0, 0x4876, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1808)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 0)
    SetChrSubChip(0xEE, 0)
    Return()

    # Function_6_17EC end

    def Function_7_183A(): pass

    label("Function_7_183A")

    SetChrChipByIndex(0xEF, 5)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 8)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 11)
    SetChrSubChip(0xF1, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F1")
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xEF, 135, 0)

    def lambda_1878():
        OP_96(0xFE, 0xFFFFE264, 0x0, 0x5A82, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1878)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF0, 45, 0)

    def lambda_18A7():
        OP_96(0xFE, 0xFFFFD9B8, 0x0, 0x47CC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_18A7)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF1, 135, 0)

    def lambda_18D6():
        OP_96(0xFE, 0xFFFFD97C, 0x0, 0x5938, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_18D6)
    Jump("loc_1A20")

    label("loc_18F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198A")
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF0, 135, 0)

    def lambda_1911():
        OP_96(0xFE, 0xFFFFE264, 0x0, 0x5A82, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1911)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xEF, 45, 0)

    def lambda_1940():
        OP_96(0xFE, 0xFFFFD9B8, 0x0, 0x47CC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1940)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF1, 135, 0)

    def lambda_196F():
        OP_96(0xFE, 0xFFFFD97C, 0x0, 0x5938, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_196F)
    Jump("loc_1A20")

    label("loc_198A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A20")
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF1, 135, 0)

    def lambda_19AA():
        OP_96(0xFE, 0xFFFFE264, 0x0, 0x5A82, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_19AA)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xEF, 45, 0)

    def lambda_19D9():
        OP_96(0xFE, 0xFFFFD9B8, 0x0, 0x47CC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_19D9)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF0, 135, 0)

    def lambda_1A08():
        OP_96(0xFE, 0xFFFFD97C, 0x0, 0x5938, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1A08)

    label("loc_1A20")

    WaitChrThread(0xEF, 0x1)
    WaitChrThread(0xF0, 0x1)
    WaitChrThread(0xF1, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 3)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 6)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 9)
    SetChrSubChip(0xF1, 0)
    Return()

    # Function_7_183A end

    def Function_8_1A5D(): pass

    label("Function_8_1A5D")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -4300, 0, 19850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1A9D():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A9D)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -6300, 0, 19650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1AF4():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1AF4)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -8300, 0, 19450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1B4B():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B4B)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -10300, 0, 19250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1BA2():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BA2)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -12300, 0, 19050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1BF9():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BF9)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -14300, 0, 18850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1C50():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C50)
    Sleep(100)
    Return()

    # Function_8_1A5D end

    def Function_9_1C68(): pass

    label("Function_9_1C68")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -4300, 0, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -6300, 0, 21150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -8300, 0, 20950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -10300, 0, 20750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -12300, 0, 20550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_23(0x235)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -14300, 0, 20350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Return()

    # Function_9_1C68 end

    def Function_10_1DE6(): pass

    label("Function_10_1DE6")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -8300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -10300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -12300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -14300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -16300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -18300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -20300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -22300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -24300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -26300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -28300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Return()

    # Function_10_1DE6 end

    def Function_11_209C(): pass

    label("Function_11_209C")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -8300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -10300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -12300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -14300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -16300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -18300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -20300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -22300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -24300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -26300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -28300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_44(0x10, 0x3)
    Return()

    # Function_11_209C end

    def Function_12_2356(): pass

    label("Function_12_2356")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2389")
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    Jump("Function_12_2356")

    label("loc_2389")

    Return()

    # Function_12_2356 end

    SaveToFile()

Try(main)
