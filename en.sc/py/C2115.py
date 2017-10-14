from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2115   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2115.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10560 ._CH',             # 00
        'ED6_DT09/CH10561 ._CH',             # 01
        'ED6_DT09/CH10570 ._CH',             # 02
        'ED6_DT09/CH10571 ._CH',             # 03
        'ED6_DT09/CH10580 ._CH',             # 04
        'ED6_DT09/CH10581 ._CH',             # 05
        'ED6_DT09/CH10590 ._CH',             # 06
        'ED6_DT09/CH10591 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10560P._CP',             # 00
        'ED6_DT09/CH10561P._CP',             # 01
        'ED6_DT09/CH10570P._CP',             # 02
        'ED6_DT09/CH10571P._CP',             # 03
        'ED6_DT09/CH10580P._CP',             # 04
        'ED6_DT09/CH10581P._CP',             # 05
        'ED6_DT09/CH10590P._CP',             # 06
        'ED6_DT09/CH10591P._CP',             # 07
    )

    DeclMonster(
        X                   = 3970,
        Z                   = 0,
        Y                   = 3770,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B9,
        Unknown_18          = 4953,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -8230,
        TriggerZ            = 0,
        TriggerY            = 8330,
        TriggerRange        = 1000,
        ActorX              = -8730,
        ActorZ              = 0,
        ActorY              = 8830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9350,
        TriggerZ            = 0,
        TriggerY            = 9330,
        TriggerRange        = 1000,
        ActorX              = 8850,
        ActorZ              = 0,
        ActorY              = 8830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12530,
        TriggerZ            = 0,
        TriggerY            = -660,
        TriggerRange        = 1000,
        ActorX              = 12530,
        ActorZ              = 0,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12430,
        TriggerZ            = 0,
        TriggerY            = -640,
        TriggerRange        = 1000,
        ActorX              = -12400,
        ActorZ              = 0,
        ActorY              = 150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4470,
        TriggerZ            = 0,
        TriggerY            = 22500,
        TriggerRange        = 1000,
        ActorX              = 4690,
        ActorZ              = 0,
        ActorY              = 23200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3680,
        TriggerZ            = 380,
        TriggerY            = 490,
        TriggerRange        = 1000,
        ActorX              = 10,
        ActorZ              = 380,
        ActorY              = 180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_1DF",          # 01, 1
        "Function_2_2A1",          # 02, 2
        "Function_3_3D8",          # 03, 3
        "Function_4_536",          # 04, 4
        "Function_5_664",          # 05, 5
        "Function_6_7B1",          # 06, 6
        "Function_7_9AF",          # 07, 7
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Return()

    # Function_0_1DE end

    def Function_1_1DF(): pass

    label("Function_1_1DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1")
    OP_6F(0x0, 0)
    Jump("loc_1F8")

    label("loc_1F1")

    OP_6F(0x0, 60)

    label("loc_1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A")
    OP_6F(0x1, 0)
    Jump("loc_211")

    label("loc_20A")

    OP_6F(0x1, 60)

    label("loc_211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223")
    OP_6F(0x2, 0)
    Jump("loc_22A")

    label("loc_223")

    OP_6F(0x2, 60)

    label("loc_22A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C")
    OP_6F(0x3, 0)
    Jump("loc_243")

    label("loc_23C")

    OP_6F(0x3, 60)

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255")
    OP_6F(0x4, 0)
    Jump("loc_25C")

    label("loc_255")

    OP_6F(0x4, 60)

    label("loc_25C")

    OP_E0(0x2, 0xA2, 0x30, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x6A, 0x4, 0x0, 0x0)
    OP_E0(0x3, 0x5E, 0xCF, 0xFF, 0xFF, 0x0, 0x0, 0x0, 0x0, 0x6A, 0x4, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26B, 1)), scpexpr(EXPR_END)), "loc_284")
    SetChrFlags(0x8, 0x80)

    label("loc_284")

    SoundDistance(0x1CB, 0xFFFFFFA6, 0x0, 0x96, 0x7D0, 0x61A8, 0x64, 0x0)
    Return()

    # Function_1_1DF end

    def Function_2_2A1(): pass

    label("Function_2_2A1")

    OP_EA(0x2, 0x89, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_379")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x177, 1)"), scpexpr(EXPR_END)), "loc_312")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x77\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1316)
    Jump("loc_376")

    label("loc_312")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x77\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x77\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_376")

    Jump("loc_3CA")

    label("loc_379")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Well, it's been swell. See you again on New Game+.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3CA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2A1 end

    def Function_3_3D8(): pass

    label("Function_3_3D8")

    OP_EA(0x2, 0x8A, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x168, 1)"), scpexpr(EXPR_END)), "loc_449")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x68\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1318)
    Jump("loc_4AD")

    label("loc_449")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x68\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x68\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4AD")

    Jump("loc_528")

    label("loc_4B0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05As you approach, the chest bursts open on its\x01",
            "own! Unfortunately, there's nothing inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_528")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3D8 end

    def Function_4_536(): pass

    label("Function_4_536")

    OP_EA(0x2, 0x8B, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x133, 1)"), scpexpr(EXPR_END)), "loc_5A7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\x33\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x131A)
    Jump("loc_60B")

    label("loc_5A7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\x33\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x33\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_60B")

    Jump("loc_656")

    label("loc_60E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Inside the chest is the key to its heart.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_656")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_536 end

    def Function_5_664(): pass

    label("Function_5_664")

    OP_EA(0x2, 0x8C, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16, 1)"), scpexpr(EXPR_END)), "loc_6D5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\x16\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x131C)
    Jump("loc_739")

    label("loc_6D5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\x16\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x16\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_739")

    Jump("loc_7A3")

    label("loc_73C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05You obtain the Sword of the Ancient\x01",
            "God-Kings. Just kidding, it's empty.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7A3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_664 end

    def Function_6_7B1(): pass

    label("Function_6_7B1")

    OP_EA(0x2, 0x8D, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_889")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1EC, 1)"), scpexpr(EXPR_END)), "loc_822")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xEC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x131F)
    Jump("loc_886")

    label("loc_822")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xEC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xEC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_886")

    Jump("loc_920")

    label("loc_889")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05This chest is empty. You vaguely remember\x01",
            "digging through it and pillaging everything it\x01",
            "had. You can't remember when...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_920")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x28)"), scpexpr(EXPR_END)), "loc_93F")
    Jump("loc_9A6")

    label("loc_93F")


    AnonymousTalk(    #15
        (
            "\x07\x00Found a scrap of paper with a [ #492i ]\x01",
            "recipe written on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #16
        "\x07\x00Learned [ #492i ] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_9A6")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7B1 end

    def Function_7_9AF(): pass

    label("Function_7_9AF")

    EventBegin(0x1)

    ChrTalk(    #17
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_9DB():
        OP_6D(-1110, 380, 470, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9DB)

    def lambda_9F3():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9F3)

    def lambda_A0B():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A0B)

    def lambda_A1B():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A1B)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E")
    OP_C0(0xE, 0x1D, 0xFFFFF40C, 0x370, 0x1D6, 0x5A, 0xFFFFFC36, 0xFFFFFE0C, 0x262)
    Fade(500)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrChipByIndex(0x0, 65535)
    ClearChrFlags(0x0, 0x2)
    ClearChrFlags(0x0, 0x40)
    ClearChrFlags(0x0, 0x4)
    SetChrPos(0x0, -3760, 380, 160, 90)
    SetChrPos(0x1, -3760, 380, 160, 90)
    SetChrPos(0x2, -3760, 380, 160, 90)
    SetChrPos(0x3, -3760, 380, 160, 90)
    SetChrPos(0x4, -3760, 380, 160, 90)
    SetChrPos(0x5, -3760, 380, 160, 90)
    SetChrPos(0x6, -3760, 380, 160, 90)
    SetChrPos(0x7, -3760, 380, 160, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_B9D")

    label("loc_B8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9D")
    EventEnd(0x1)

    label("loc_B9D")

    Return()

    # Function_7_9AF end

    SaveToFile()

Try(main)
