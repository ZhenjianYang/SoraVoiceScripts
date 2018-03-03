from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M3203   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3203.x',
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
        'General Morgan',                       # 9
        'Royal Army Officer',                   # 10
        'Royal Army Officer',                   # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT07/CH02080 ._CH',             # 00
        'ED6_DT27/CH04430 ._CH',             # 01
        'ED6_DT27/CH04431 ._CH',             # 02
        'ED6_DT27/CH04434 ._CH',             # 03
        'ED6_DT27/CH04435 ._CH',             # 04
        'ED6_DT07/CH00330 ._CH',             # 05
        'ED6_DT07/CH00331 ._CH',             # 06
        'ED6_DT07/CH00430 ._CH',             # 07
        'ED6_DT07/CH00431 ._CH',             # 08
        'ED6_DT09/CH10060 ._CH',             # 09
        'ED6_DT09/CH10061 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02080P._CP',             # 00
        'ED6_DT27/CH04430P._CP',             # 01
        'ED6_DT27/CH04431P._CP',             # 02
        'ED6_DT27/CH04434P._CP',             # 03
        'ED6_DT27/CH04435P._CP',             # 04
        'ED6_DT07/CH00330P._CP',             # 05
        'ED6_DT07/CH00331P._CP',             # 06
        'ED6_DT07/CH00430P._CP',             # 07
        'ED6_DT07/CH00431P._CP',             # 08
        'ED6_DT09/CH10060P._CP',             # 09
        'ED6_DT09/CH10061P._CP',             # 0A
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -40800,
        Z                   = 0,
        Y                   = 21190,
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
        X                   = -67070,
        Z                   = 0,
        Y                   = 2120,
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
        X                   = 1110,
        Z                   = 0,
        Y                   = -48520,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 1060,
        TriggerZ            = 0,
        TriggerY            = 5760,
        TriggerRange        = 1000,
        ActorX              = 1060,
        ActorZ              = 800,
        ActorY              = 5760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30940,
        TriggerZ            = 0,
        TriggerY            = -48030,
        TriggerRange        = 1000,
        ActorX              = 30940,
        ActorZ              = 1000,
        ActorY              = -48030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39470,
        TriggerZ            = 120,
        TriggerY            = 43240,
        TriggerRange        = 1000,
        ActorX              = -39470,
        ActorZ              = 1120,
        ActorY              = 43240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 39920,
        TriggerZ            = 120,
        TriggerY            = 1330,
        TriggerRange        = 1000,
        ActorX              = 39920,
        ActorZ              = 1120,
        ActorY              = 1330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 39930,
        TriggerZ            = 120,
        TriggerY            = -1080,
        TriggerRange        = 1000,
        ActorX              = 39930,
        ActorZ              = 1120,
        ActorY              = -1080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4130,
        TriggerZ            = 0,
        TriggerY            = 34910,
        TriggerRange        = 1000,
        ActorX              = 4130,
        ActorZ              = 2000,
        ActorY              = 34910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28E",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_32E",          # 02, 2
        "Function_3_465",          # 03, 3
        "Function_4_5AF",          # 04, 4
        "Function_5_721",          # 05, 5
        "Function_6_860",          # 06, 6
        "Function_7_966",          # 07, 7
        "Function_8_96F",          # 08, 8
        "Function_9_2AE5",         # 09, 9
        "Function_10_2B3A",        # 0A, 10
        "Function_11_2B8F",        # 0B, 11
        "Function_12_478B",        # 0C, 12
        "Function_13_484A",        # 0D, 13
    )


    def Function_0_28E(): pass

    label("Function_0_28E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B3")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_2B3")

    Return()

    # Function_0_28E end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB")
    OP_6F(0x38, 0)
    Jump("loc_2E2")

    label("loc_2DB")

    OP_6F(0x38, 60)

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4")
    OP_6F(0x39, 0)
    Jump("loc_2FB")

    label("loc_2F4")

    OP_6F(0x39, 60)

    label("loc_2FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D")
    OP_6F(0x3A, 0)
    Jump("loc_314")

    label("loc_30D")

    OP_6F(0x3A, 60)

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326")
    OP_6F(0x3B, 0)
    Jump("loc_32D")

    label("loc_326")

    OP_6F(0x3B, 60)

    label("loc_32D")

    Return()

    # Function_1_2B4 end

    def Function_2_32E(): pass

    label("Function_2_32E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x38, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x336, 1)"), scpexpr(EXPR_END)), "loc_39C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x36\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B90)
    Jump("loc_404")

    label("loc_39C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x36\x03\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x36\x03\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x38, 60)
    OP_70(0x38, 0x0)

    label("loc_404")

    Jump("loc_457")

    label("loc_407")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Fine. Take it! I don't even want it anymore!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x2A, 0x0)

    label("loc_457")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_32E end

    def Function_3_465(): pass

    label("Function_3_465")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x39, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_4D3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x01\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B91)
    Jump("loc_53B")

    label("loc_4D3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x01\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x01\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x39, 60)
    OP_70(0x39, 0x0)

    label("loc_53B")

    Jump("loc_5A1")

    label("loc_53E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05My vocal instructor told me I should use my chest voice more...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x2B, 0x0)

    label("loc_5A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_465 end

    def Function_4_5AF(): pass

    label("Function_4_5AF")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3A, 0x1E)
    OP_73(0x3A)
    OP_6F(0x3A, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #6
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
    OP_A2(0x2B92)
    Jump("loc_70A")

    label("loc_6BF")


    AnonymousTalk(    #7
        "\x07\x05I should have listened to my parents and become a cupboard instead.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_70A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x2C, 0x0)
    Return()

    # Function_4_5AF end

    def Function_5_721(): pass

    label("Function_5_721")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_78F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B93)
    Jump("loc_7F7")

    label("loc_78F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3B, 60)
    OP_70(0x3B, 0x0)

    label("loc_7F7")

    Jump("loc_852")

    label("loc_7FA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05This chest is empty, but it smells pleasantly minty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x2D, 0x0)

    label("loc_852")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_721 end

    def Function_6_860(): pass

    label("Function_6_860")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #11
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 0)), scpexpr(EXPR_END)), "loc_962")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_962")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Use C-02 Key\x01",      # 0
            "Cancel\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_92E"),
        (SWITCH_DEFAULT, "loc_952"),
    )


    label("loc_92E")

    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_A2(0x2B82)
    OP_71(0x1004, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95F")

    label("loc_952")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95F")

    label("loc_95F")

    Jump("loc_8DE")

    label("loc_962")

    TalkEnd(0xFF)
    Return()

    # Function_6_860 end

    def Function_7_966(): pass

    label("Function_7_966")

    Call(0, 8)
    Call(0, 11)
    Return()

    # Function_7_966 end

    def Function_8_96F(): pass

    label("Function_8_96F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x4B, 0x2)
    OP_E0(238, 0x4C, 0x3)
    OP_E0(239, 0x4D, 0x2)
    OP_E0(239, 0x4E, 0x3)
    OP_E0(240, 0x4F, 0x2)
    OP_E0(240, 0x50, 0x3)
    OP_E0(241, 0x51, 0x2)
    OP_E0(241, 0x52, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 610, 0, 78790, 180)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -170, 0, 65019, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4F")
    SetChrPos(0xEF, 1490, 0, 65030, 0)
    SetChrPos(0xF0, -640, 0, 63180, 0)
    SetChrPos(0xF1, 1650, 0, 63540, 0)
    Jump("loc_AD4")

    label("loc_A4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A93")
    SetChrPos(0xF0, 1490, 0, 65030, 0)
    SetChrPos(0xEF, -640, 0, 63180, 0)
    SetChrPos(0xF1, 1650, 0, 63540, 0)
    Jump("loc_AD4")

    label("loc_A93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD4")
    SetChrPos(0xF1, 1490, 0, 65030, 0)
    SetChrPos(0xEF, -640, 0, 63180, 0)
    SetChrPos(0xF0, 1650, 0, 63540, 0)

    label("loc_AD4")

    OP_6D(1590, 0, 65300, 0)
    OP_67(0, 5870, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(45000, 0)
    OP_6E(290, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #12
        0x10,
        "Old Man's Voice",
        (
            "#4S#4PWhat time do you call this?!\x01",
            "You're late! All of you!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C28")

    label("loc_BC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE9")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C28")

    label("loc_BE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C11")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C28")

    label("loc_C11")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C28")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CBC")

    label("loc_C55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CBC")

    label("loc_C7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA5")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CBC")

    label("loc_CA5")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CBC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE9")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D50")

    label("loc_CE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D11")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D50")

    label("loc_D11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D39")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D50")

    label("loc_D39")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D50")

    Sleep(1000)

    ChrTalk(    #13
        0x109,
        "#1064F#6PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10C,
        "#112F#12PGeneral Morgan?!\x02",
    )

    CloseMessageWindow()

    def lambda_D91():
        OP_8F(0xFE, 0xFFFFFDF8, 0x0, 0x11A8A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D91)
    Sleep(100)

    def lambda_DB1():
        OP_6D(1530, 0, 75920, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_DB1)

    def lambda_DC9():
        OP_67(0, 5080, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_DC9)

    def lambda_DE1():
        OP_6B(2480, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_DE1)

    def lambda_DF1():
        OP_6E(341, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_DF1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E67")

    def lambda_E0F():
        OP_8F(0xFE, 0x442, 0x0, 0x11A3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_E0F)
    Sleep(100)

    def lambda_E2F():
        OP_8F(0xFE, 0xFFFFFC2C, 0x0, 0x11350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_E2F)
    Sleep(100)

    def lambda_E4F():
        OP_8F(0xFE, 0x514, 0x0, 0x1135A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_E4F)
    Jump("loc_F3C")

    label("loc_E67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED3")

    def lambda_E7B():
        OP_8F(0xFE, 0x442, 0x0, 0x11A3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_E7B)
    Sleep(100)

    def lambda_E9B():
        OP_8F(0xFE, 0xFFFFFC2C, 0x0, 0x11350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_E9B)
    Sleep(100)

    def lambda_EBB():
        OP_8F(0xFE, 0x514, 0x0, 0x1135A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_EBB)
    Jump("loc_F3C")

    label("loc_ED3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3C")

    def lambda_EE7():
        OP_8F(0xFE, 0x442, 0x0, 0x11A3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_EE7)
    Sleep(100)

    def lambda_F07():
        OP_8F(0xFE, 0xFFFFFC2C, 0x0, 0x11350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_F07)
    Sleep(100)

    def lambda_F27():
        OP_8F(0xFE, 0x514, 0x0, 0x1135A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_F27)

    label("loc_F3C")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #15
        0x10,
        (
            "#163F#5PWhat is the meaning of all of this?!\x02\x03",

            "#166FI get dragged here by some bizarre masked hoodlum,\x01",
            "stripped of my free will, and am now being used like\x01",
            "some sort of puppet! This is humiliating!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #16
        0x10,
        "#162F#5P#3SI've never been so damned infuriated in all my years!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A9")
    OP_62(0xEE, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1110")

    label("loc_10A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D1")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1110")

    label("loc_10D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F9")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1110")

    label("loc_10F9")

    OP_62(0xEE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1110")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1138")
    OP_62(0xEF, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_119F")

    label("loc_1138")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1160")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_119F")

    label("loc_1160")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1188")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_119F")

    label("loc_1188")

    OP_62(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_119F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C7")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_122E")

    label("loc_11C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EF")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_122E")

    label("loc_11EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1217")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_122E")

    label("loc_1217")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_122E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1256")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_12BD")

    label("loc_1256")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127E")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_12BD")

    label("loc_127E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A6")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_12BD")

    label("loc_12A6")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_12BD")

    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12ED")

    ChrTalk(    #17
        0x105,
        "#1163F#12PGeneral...\x02",
    )

    CloseMessageWindow()
    Jump("loc_135B")

    label("loc_12ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1317")

    ChrTalk(    #18
        0x10E,
        "#178F#12PGeneral...\x02",
    )

    CloseMessageWindow()
    Jump("loc_135B")

    label("loc_1317")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1342")

    ChrTalk(    #19
        0x102,
        "#1502F#12PGeneral...\x02",
    )

    CloseMessageWindow()
    Jump("loc_135B")

    label("loc_1342")


    ChrTalk(    #20
        0x10C,
        "#112F#12PGeneral...\x02",
    )

    CloseMessageWindow()

    label("loc_135B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1392")

    ChrTalk(    #21
        0x101,
        "#1007F#12PYou haven't changed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_1392")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CB")

    ChrTalk(    #22
        0x106,
        "#556F#12PHeh. YOU haven't changed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_13CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1410")

    ChrTalk(    #23
        0x103,
        "#1534F#12PHaha. I see you're the same as ever.\x02",
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_1410")


    ChrTalk(    #24
        0x109,
        "#1066F#6PHaha... Looks like he hasn't changed a bit.\x02",
    )

    CloseMessageWindow()

    label("loc_144A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1494")

    ChrTalk(    #25
        0x104,
        "#1545F#12PHeh. Your voice is as boisterous as ever.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DC")

    label("loc_1494")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14DC")

    ChrTalk(    #26
        0x108,
        "#573F#12PHaha... That was one hell of a roar, there.\x02",
    )

    CloseMessageWindow()

    label("loc_14DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152E")

    ChrTalk(    #27
        0x110,
        (
            "#264F#12PWow... This old man sure has impressive\x01",
            "vocal chords.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1571")

    ChrTalk(    #28
        0x10B,
        "#216F#12PBoy... This is one hotblooded old man.\x02",
    )

    CloseMessageWindow()

    label("loc_1571")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1598")

    ChrTalk(    #29
        0x107,
        "#067F#12PA-Ahaha...\x02",
    )

    CloseMessageWindow()

    label("loc_1598")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E4")

    ChrTalk(    #30
        0x10A,
        "#819F#12PTh-This guy's as scary as all the rumors say...\x02",
    )

    CloseMessageWindow()

    label("loc_15E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161C")

    ChrTalk(    #31
        0x10F,
        "#1803F#12P(His voice is too loud...)\x02",
    )

    CloseMessageWindow()

    label("loc_161C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1679")

    ChrTalk(    #32
        0x10D,
        (
            "#270F#4P(So our next opponent is perhaps Liberl's most\x01",
            "famous officer...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1679")


    ChrTalk(    #33
        0x10,
        (
            "#163F#5PWell, I suppose getting angry won't do me\x01",
            "any good.\x02\x03",

            "#160FYou all have my sympathies for the situation\x01",
            "you've been forced into.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1823")
    Sleep(500)

    ChrTalk(    #34
        0x10,
        (
            "#163F#5PI see you're here, too, Agate Crosner... \x01",
            "and Professor Russell's granddaughter.\x02\x03",

            "#165FI thought if it were to run into you two again,\x01",
            "it wouldn't be in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x107,
        "#560F#12PWell, erm...it's good to see you, sir!\x02",
    )

    CloseMessageWindow()
    Jump("loc_18C1")

    label("loc_1823")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18C1")
    Sleep(500)

    ChrTalk(    #36
        0x10,
        (
            "#163F#5PI see you're here, too, Agate Crosner.\x02\x03",

            "#165FI thought if it were to run into you again,\x01",
            "it wouldn't be in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C1")


    ChrTalk(    #37
        0x106,
        (
            "#051F#12PHeh. You got me, there. I've heard all kindsa\x01",
            "stuff about you since we last met, though.\x02\x03",

            "Been told there was a point where you were\x01",
            "known far and wide as Liberl's God of War...\x01",
            "That true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        "#165F#5PHmph. That was a long time ago.\x02",
    )

    CloseMessageWindow()

    label("loc_19B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D7C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ADB")
    Sleep(500)

    ChrTalk(    #39
        0x10,
        (
            "#163F#5PSo, Estelle and Joshua Bright...\x02\x03",

            "#165FHow have you been faring on your journey?\x01",
            "Are you still doing well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1016F#12PAhaha... Yeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#1514F#12PI'm glad to see you're still in good health,\x01",
            "too, General.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9A")

    label("loc_1ADB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC3")
    Sleep(500)

    ChrTalk(    #42
        0x10,
        (
            "#163F#5PSo, Estelle Bright...\x02\x03",

            "#165FHow have you been faring on your journey?\x01",
            "Are you still doing well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1016F#12PAhaha... Yeah, thanks.\x02\x03",

            "#1006FYou look like you're doing all right, too.\x01",
            "That's good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9A")

    label("loc_1BC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C9A")
    Sleep(500)

    ChrTalk(    #44
        0x10,
        (
            "#163F#5PSo, Joshua Bright...\x02\x03",

            "#165FHow have you been faring on your journey?\x01",
            "Are you still doing well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#1513F#12PYes, thank you.\x02\x03",

            "#1500FI'm glad to see you're still in good health,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9A")


    ChrTalk(    #46
        0x10,
        (
            "#163F#5PBah. I'm past my prime.\x02\x03",

            "#165FThe sooner I can pass my duties over\x01",
            "to your father and retire, the better.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D37")

    ChrTalk(    #47
        0x101,
        "#1008F#12PAhaha...\x02",
    )

    CloseMessageWindow()

    label("loc_1D37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D7C")

    ChrTalk(    #48
        0x102,
        "#1513F#12P...I'm sure you've more than earned it.\x02",
    )

    CloseMessageWindow()

    label("loc_1D7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21B7")
    Sleep(500)

    ChrTalk(    #49
        0x10,
        (
            "#163F#5PAbove all, however...it brings me great shame to\x01",
            "think that Her Highness Princess Klaudia became\x01",
            "a victim of all of this...\x02\x03",

            "#166FI'm disgusted with myself as an officer for being\x01",
            "unable to prevent it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FAD")

    ChrTalk(    #50
        0x10E,
        (
            "#179F#12PPlease do not worry about Princess Klaudia,\x01",
            "Your Excellency.\x02\x03",

            "#170FI will protect her and be sure that she leaves\x01",
            "here safely, even if it costs me my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x105,
        "#1382F#12PI wouldn't want you going that far, Julia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        "#165F#5PWell, that brings me some comfort, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B7")

    label("loc_1FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20A2")

    ChrTalk(    #53
        0x10E,
        (
            "#179F#12PPlease do not worry about Princess Klaudia,\x01",
            "Your Excellency.\x02\x03",

            "#170FI will protect her and be sure that she leaves\x01",
            "here safely, even if it costs me my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        "#165F#5PWell, that brings me some comfort, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B7")

    label("loc_20A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21B7")

    ChrTalk(    #55
        0x105,
        (
            "#1383F#12PI would ask that you not worry about me, General.\x02\x03",

            "#1382FI have Julia supporting me. I will return safely--\x01",
            "I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        (
            "#161F#5PTruly, Your Highness?\x02\x03",

            "#165FThen I shall cast my worries aside for now.\x01",
            "May the Goddess watch over and protect you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B7")

    Sleep(500)

    ChrTalk(    #57
        0x10,
        (
            "#163F#5P...Richard.\x02\x03",

            "I have plenty I want to say to you, and a lot I could\x01",
            "say to you...\x02\x03",

            "#165F...but I'm not sure I'm the best person to do so,\x01",
            "so I'll let you off for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10C,
        "#115F#12P...Thank you, General.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "#163F#5PRegardless, I think we've wasted enough time talking.\x02\x03",

            "#160FThere's no avoiding a battle between us--we may as\x01",
            "well get started on it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_2338():
        OP_6D(1800, 0, 76920, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2338)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A3")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_240A")

    label("loc_23A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23CB")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_240A")

    label("loc_23CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23F3")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_240A")

    label("loc_23F3")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_240A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2437")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_249E")

    label("loc_2437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245F")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_249E")

    label("loc_245F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2487")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_249E")

    label("loc_2487")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_249E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24CB")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2532")

    label("loc_24CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24F3")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2532")

    label("loc_24F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2532")

    label("loc_251B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2532")

    Sleep(1000)

    ChrTalk(    #60
        0x109,
        (
            "#1063F#6PA-A halberd? Aidios, I'm not sure when I last\x01",
            "saw one of those...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10C,
        (
            "#114F#12PDon't underestimate his weapon! In his hands,\x01",
            "it is extremely deadly!\x02\x03",

            "Before the mechanization of the army began,\x01",
            "that halberd claimed the lives of countless foes\x01",
            "on the battlefield!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10, 4)

    def lambda_2662():

        label("loc_2662")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2662")

    QueueWorkItem2(0x10, 3, lambda_2662)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -1790, 100, 79330, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 2990, 100, 79080, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_271E():
        OP_6D(1610, 0, 76300, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_271E)

    def lambda_2736():
        OP_67(0, 5960, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2736)

    def lambda_274E():
        OP_6B(2360, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_274E)

    def lambda_275E():
        OP_6E(373, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_275E)

    def lambda_276E():
        OP_6C(32000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_276E)
    Sleep(500)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -1790, -3000, 79330, 180)
    SetChrPos(0x12, 2990, -3000, 79080, 180)
    OP_22(0x85, 0x1, 0x64)

    def lambda_27B4():

        label("loc_27B4")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_27B4")

    QueueWorkItem2(0x109, 3, lambda_27B4)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x12, 0x0, 0x0, 0xA)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 11)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 13)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 15)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 17)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_23(0x85)
    OP_82(0x0, 0x2)
    OP_44(0x10, 0x3)
    OP_44(0x109, 0x3)
    OP_1D(0xC4)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #62
        0x10,
        (
            "#165F#5PHah. I haven't had cause to wield this since the\x01",
            "martial arts tournament two years ago, however.\x02\x03",

            "#163FBut if you struggle against an old man like me,\x01",
            "your odds of success in the trials ahead are grim\x01",
            "indeed.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #63
        0x10,
        "#162F#5P#4SDon't hold back! Show me what you've got!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_29A3():
        OP_6D(1130, 0, 75700, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_29A3)

    def lambda_29BB():
        OP_67(0, 6370, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_29BB)

    def lambda_29D3():
        OP_6B(2050, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_29D3)

    def lambda_29E3():
        OP_6E(300, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_29E3)
    SetChrChipByIndex(0x10, 2)

    def lambda_29F8():
        OP_8F(0xFE, 0x258, 0x0, 0x11DA0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_29F8)
    Sleep(10)
    SetChrChipByIndex(0x11, 6)

    def lambda_2A1D():
        OP_8F(0xFE, 0xFFFFFD9E, 0x0, 0x12066, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2A1D)
    Sleep(10)
    SetChrChipByIndex(0x12, 8)

    def lambda_2A42():
        OP_8F(0xFE, 0x67C, 0x0, 0x120AC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_2A42)

    def lambda_2A5D():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2A5D)

    def lambda_2A78():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2A78)

    def lambda_2A93():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2A93)

    def lambda_2AAE():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2AAE)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A9, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_8_96F end

    def Function_9_2AE5(): pass

    label("Function_9_2AE5")

    PlayEffect(0x1, 0x3, 0xFF, -1790, 100, 79330, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x3, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_2AE5 end

    def Function_10_2B3A(): pass

    label("Function_10_2B3A")

    PlayEffect(0x1, 0x4, 0xFF, 2990, 100, 79080, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_2B3A end

    def Function_11_2B8F(): pass

    label("Function_11_2B8F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 610, 0, 78790, 180)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 3)
    OP_43(0x10, 0x3, 0x0, 0xC)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 50, 500, 100, 0, 0, 0, 2300, 2500, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -150, 0, 74920, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CAB")
    SetChrPos(0xEF, 1300, 0, 74940, 0)
    SetChrPos(0xF0, -600, 0, 73160, 0)
    SetChrPos(0xF1, 1010, 0, 73260, 0)
    Jump("loc_2D30")

    label("loc_2CAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEF")
    SetChrPos(0xF0, 1300, 0, 74940, 0)
    SetChrPos(0xEF, -600, 0, 73160, 0)
    SetChrPos(0xF1, 1010, 0, 73260, 0)
    Jump("loc_2D30")

    label("loc_2CEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D30")
    SetChrPos(0xF1, 1300, 0, 74940, 0)
    SetChrPos(0xEF, -600, 0, 73160, 0)
    SetChrPos(0xF0, 1010, 0, 73260, 0)

    label("loc_2D30")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(2100, 0, 77960, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #64
        0x10,
        (
            "#163F#5PHaha... Well, that's something of a relief...\x02\x03",

            "#165FPerhaps you might be able to pull off a miracle\x01",
            "with that strength...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10C,
        "#112F#12PThen our final foe is who I fear it is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#163F#5PIndeed, it is.\x02\x03",

            "#160FAnd no matter how strong he may be, he is\x01",
            "human like the rest of us; no man is invincible.\x02\x03",

            "Pour everything you have into the battle, and\x01",
            "you may yet be able to defeat him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10C,
        "#119F#12P...Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        (
            "#163F#5PHaha... Still, I'm a little disappointed...\x02\x03",

            "The thought that he may actually be defeated\x01",
            "in battle and I won't be there to see it happen\x01",
            "is a frustrating one.\x02\x03",

            "#165FShould we ever meet again, I'd like to know how\x01",
            "the battle went.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, -100, -850, 0, 0, 0, 0, 1900, 1900, 1900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_309C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_309C)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    Sleep(1000)

    ChrTalk(    #69
        0x10C,
        "#116F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1067F#6PWell, it sounds like we're in for the fight of\x01",
            "our lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10C,
        (
            "#115F#11PThat it will be...\x02\x03",

            "#110FI suspect this was always an inevitability.\x01",
            "...Especially as long as I am here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_319A():
        OP_6D(2240, 0, 76000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_319A)

    def lambda_31B2():
        OP_67(0, 5160, -10000, 1200)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_31B2)

    def lambda_31CA():
        OP_6B(2440, 1200)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_31CA)

    def lambda_31DA():
        OP_6E(322, 1200)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_31DA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3222")

    def lambda_31F8():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_31F8)
    Sleep(100)

    def lambda_320B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_320B)
    Sleep(100)
    OP_8C(0xF0, 45, 400)
    Jump("loc_329B")

    label("loc_3222")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3260")

    def lambda_3236():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3236)
    Sleep(100)

    def lambda_3249():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3249)
    Sleep(100)
    OP_8C(0xEF, 45, 400)
    Jump("loc_329B")

    label("loc_3260")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_329B")

    def lambda_3274():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3274)
    Sleep(100)

    def lambda_3287():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3287)
    Sleep(100)
    OP_8C(0xEF, 45, 400)

    label("loc_329B")

    WaitChrThread(0xEE, 0x3)
    Sleep(400)

    ChrTalk(    #72
        0x10C,
        (
            "#115F#5PI may not be in any position to ask, but I'd\x01",
            "appreciate it if you would all lend me your \x01",
            "strength.\x02\x03",

            "#112FThis battle should allow me to finally put the \x01",
            "past behind me so I can truly move forward...\x01",
            "but I can't win it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x109,
        (
            "#1840F#6PHaha... After a plea like that, how could we\x01",
            "refuse?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_344D")

    ChrTalk(    #74
        0x101,
        (
            "#1012F#6PI'd be happy to!\x02\x03",

            "#1006FI'm curious how much of a fight I can put up\x01",
            "against him, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_344D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3500")

    ChrTalk(    #75
        0x102,
        (
            "#1513F#6PI'd be happy to.\x02\x03",

            "#1501FIt's been six years now since he took me in...\x01",
            "This will be a good chance to show him how\x01",
            "much I've grown during that time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3500")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35BA")

    ChrTalk(    #76
        0x103,
        (
            "#1521F#6PHaha. Of course.\x02\x03",

            "#1536FI can't say I'm not afraid to fight him, but as\x01",
            "his former student, it will be a good chance\x01",
            "to show him just how much I've grown.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_35BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3651")

    ChrTalk(    #77
        0x106,
        (
            "#053F#6PHeh. Nothing would make me happier.\x02\x03",

            "#051FI'm curious just how much of a fight I can\x01",
            "put up against him these days, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3651")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_370E")

    ChrTalk(    #78
        0x108,
        (
            "#573F#6PIt'd be my pleasure.\x02\x03",

            "#070FI'd love to see how effective my Taito skills \x01",
            "are against Master Cassius. It's not a chance\x01",
            "I'm likely to get again any time soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_370E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37F7")

    ChrTalk(    #79
        0x10E,
        (
            "#179F#6PI would be honored to have the chance to fight him.\x02\x03",

            "#170FHe was the one who taught me the basics of combat\x01",
            "at military academy... I would very much like to show\x01",
            "him how much I have built on them since.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_37F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38C4")

    ChrTalk(    #80
        0x10A,
        (
            "#1316F#6PI-I'm really not sure I stand a chance against him...\x02\x03",

            "#816FBut as a fellow Eight Leaves practitioner, I'm not\x01",
            "going to let a chance to try my skills against him\x01",
            "pass me by!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_38C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3973")

    ChrTalk(    #81
        0x10D,
        (
            "#278F#6P...I'd be happy to.\x02\x03",

            "#275FHaving the chance to test my skills against \x01",
            "Liberl's most legendary swordsman is an \x01",
            "opportunity too good to pass on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3973")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A14")

    ChrTalk(    #82
        0x110,
        (
            "#263F#6PHeehee. So we get to fight the legendary\x01",
            "hero the professor was so scared of, huh?\x02\x03",

            "#1306FI can hardly wait to see what he's like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3A14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AE0")

    ChrTalk(    #83
        0x105,
        (
            "#1383F#6PI have no idea how well I can hold up against\x01",
            "such an esteemed figure...\x02\x03",

            "#1382F...but I have no intention of running away from\x01",
            "this challenge. I intend to face it head on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3AE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BAD")

    ChrTalk(    #84
        0x104,
        (
            "#1545F#6PIt will be an honor to face the famed strategist\x01",
            "and legendary swordsman who was able to repel\x01",
            "Erebonia during the war.\x02\x03",

            "#1540FThis should prove an...educational experience.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3BAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C72")

    ChrTalk(    #85
        0x10F,
        (
            "#1446F#6PHis name and strength are known even in\x01",
            "the Gralsritter.\x02\x03",

            "#1448FI'm not sure how well I will be able to fare\x01",
            "against him...but I intend to fight the very\x01",
            "best I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3C72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CFE")

    ChrTalk(    #86
        0x10B,
        (
            "#413F#6PTh-This next guy's really that much of a\x01",
            "big deal, huh?\x02\x03",

            "#210FStill, I'm not gonna let that stop me from\x01",
            "trying!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DA2")

    ChrTalk(    #87
        0x107,
        (
            "#563F#6PI-I don't know whether I'll be of any use...\x02\x03",

            "#560F...but I'm not going to run away! I'm going\x01",
            "to try and do what I can to help, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_3DA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E31")

    ChrTalk(    #88
        0x10B,
        (
            "#413F#6PTh-This next guy's really that much of a\x01",
            "big deal, huh?\x02\x03",

            "#210FStill, I'm not gonna let that stop me from\x01",
            "trying!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_3E31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EF6")

    ChrTalk(    #89
        0x10F,
        (
            "#1446F#6PHis name and strength are known even in\x01",
            "the Gralsritter.\x02\x03",

            "#1448FI'm not sure how well I will be able to fare\x01",
            "against him...but I intend to fight the very\x01",
            "best I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_3EF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FC3")

    ChrTalk(    #90
        0x104,
        (
            "#1545F#6PIt will be an honor to face the famed strategist\x01",
            "and legendary swordsman who was able to repel\x01",
            "Erebonia during the war.\x02\x03",

            "#1540FThis should prove an...educational experience.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_3FC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_408F")

    ChrTalk(    #91
        0x105,
        (
            "#1383F#6PI have no idea how well I can hold up against\x01",
            "such an esteemed figure...\x02\x03",

            "#1382F...but I have no intention of running away from\x01",
            "this challenge. I intend to face it head on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_408F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_412A")

    ChrTalk(    #92
        0x110,
        (
            "#260F#6PHeehee. So we get to fight the legendary\x01",
            "hero the professor was so scared of, huh?\x02\x03",

            "I can hardly wait to see what he's like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_412A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41D4")

    ChrTalk(    #93
        0x10D,
        (
            "#270F#6P...I'd be happy to.\x02\x03",

            "Having the chance to test my skills against \x01",
            "Liberl's most legendary swordsman is an \x01",
            "opportunity too good to pass on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_41D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42A1")

    ChrTalk(    #94
        0x10A,
        (
            "#1316F#6PI-I'm really not sure I stand a chance against him...\x02\x03",

            "#816FBut as a fellow Eight Leaves practitioner, I'm not\x01",
            "going to let a chance to try my skills against him\x01",
            "pass me by!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_42A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_438A")

    ChrTalk(    #95
        0x10E,
        (
            "#179F#6PI would be honored to have the chance to fight him.\x02\x03",

            "#170FHe was the one who taught me the basics of combat\x01",
            "at military academy... I would very much like to show\x01",
            "him how much I have built on them since.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_438A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_443F")

    ChrTalk(    #96
        0x108,
        (
            "#573F#6PI'm in, too.\x02\x03",

            "#070FI'd love to see how effective my Taito skills \x01",
            "are against Master Cassius. It's not a chance\x01",
            "I'm likely to get again any time soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_443F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44D6")

    ChrTalk(    #97
        0x106,
        (
            "#053F#6PHeh. I'm in, too!\x02\x03",

            "#051FI can't wait to see the look of surprise on\x01",
            "that smug mustached face of his when he\x01",
            "gets beaten!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_44D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4592")

    ChrTalk(    #98
        0x103,
        (
            "#1521F#6PHaha. I'm in, too.\x02\x03",

            "#1536FI can't say I'm not afraid to fight him, but as\x01",
            "his former student, it will be a good chance to\x01",
            "show him just how much I've grown.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464E")

    label("loc_4592")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_464E")

    ChrTalk(    #99
        0x102,
        (
            "#1513F#6PI'd be happy to assist, too.\x02\x03",

            "#1501FIt's been six years now since he took me in...\x01",
            "This will be a good chance to show him how\x01",
            "much I've grown during that time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_464E")


    ChrTalk(    #100
        0x10C,
        (
            "#111F#5P...Thank you, all of you.\x02\x03",

            "#119FOur next opponent is perhaps the strongest\x01",
            "in the land. No underhanded tricks will work\x01",
            "against him.\x02\x03",

            "#110FOur only hope is to do as the general said\x01",
            "and pour everything we have into fighting\x01",
            "him. May the Goddess smile upon us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        "#1078F#6PRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B1F)
    OP_28(0x39, 0x1, 0x80)
    OP_28(0x39, 0x1, 0x100)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_11_2B8F end

    def Function_12_478B(): pass

    label("Function_12_478B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47AC")
    Sleep(100)
    Jump("loc_4827")

    label("loc_47AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C1")
    Sleep(200)
    Jump("loc_4827")

    label("loc_47C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47D6")
    Sleep(300)
    Jump("loc_4827")

    label("loc_47D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47EB")
    Sleep(400)
    Jump("loc_4827")

    label("loc_47EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4800")
    Sleep(500)
    Jump("loc_4827")

    label("loc_4800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4815")
    Sleep(600)
    Jump("loc_4827")

    label("loc_4815")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4827")
    Sleep(700)

    label("loc_4827")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4849")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_4827")

    label("loc_4849")

    Return()

    # Function_12_478B end

    def Function_13_484A(): pass

    label("Function_13_484A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4919")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(6656)
    Sleep(500)
    Jump("loc_491C")

    label("loc_4919")

    TalkBegin(0xFF)

    label("loc_491C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #102
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4958")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A9B")

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
        (0, "loc_49B4"),
        (1, "loc_4A2F"),
        (2, "loc_4A5D"),
        (SWITCH_DEFAULT, "loc_4A8B"),
    )


    label("loc_49B4")

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
    Jump("loc_4A98")

    label("loc_4A2F")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #103
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4A98")

    label("loc_4A5D")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #104
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4A98")

    label("loc_4A8B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A98")

    label("loc_4A98")

    Jump("loc_4958")

    label("loc_4A9B")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC8")
    OP_A2(0x25A8)
    EventEnd(0x1)
    Jump("loc_4ACB")

    label("loc_4AC8")

    TalkEnd(0xFF)

    label("loc_4ACB")

    Return()

    # Function_13_484A end

    SaveToFile()

Try(main)
