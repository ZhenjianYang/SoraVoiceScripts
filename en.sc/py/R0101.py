from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0101   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0101.x',
        MapIndex            = 23,
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
        'Fog',                                  # 9
        'Rolent',                               # 10
        'Gurune Gate',                          # 11
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
        'ED6_DT09/CH10240 ._CH',             # 00
        'ED6_DT09/CH10241 ._CH',             # 01
        'ED6_DT09/CH10230 ._CH',             # 02
        'ED6_DT09/CH10231 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH10240P._CP',             # 00
        'ED6_DT09/CH10241P._CP',             # 01
        'ED6_DT09/CH10230P._CP',             # 02
        'ED6_DT09/CH10231P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35110,
        Z                   = 1000,
        Y                   = 185500,
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
        X                   = -122810,
        Z                   = 1000,
        Y                   = -720,
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


    DeclMonster(
        X                   = -32000,
        Z                   = 1000,
        Y                   = 154000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42000,
        Z                   = 1400,
        Y                   = 142000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x17,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28000,
        Z                   = 2000,
        Y                   = 120000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -47000,
        Z                   = 1000,
        Y                   = 122000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x14,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -55000,
        Z                   = 1000,
        Y                   = 106000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x15,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33000,
        Z                   = 1000,
        Y                   = 109000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -83000,
        Z                   = 2000,
        Y                   = 84900,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x17,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -94000,
        Z                   = 1000,
        Y                   = 62000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -106000,
        Z                   = 1000,
        Y                   = 42000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x14,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -125000,
        Z                   = 1000,
        Y                   = 34000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x15,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -126160,
        TriggerZ            = 1030,
        TriggerY            = 32310,
        TriggerRange        = 1000,
        ActorX              = -126630,
        ActorZ              = 1030,
        ActorY              = 32530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24690,
        TriggerZ            = 2009,
        TriggerY            = 123260,
        TriggerRange        = 1000,
        ActorX              = -24030,
        ActorZ              = 2000,
        ActorY              = 123440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -91280,
        TriggerZ            = 970,
        TriggerY            = 78610,
        TriggerRange        = 1000,
        ActorX              = -96410,
        ActorZ              = -500,
        ActorY              = 77750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_2DF",          # 01, 1
        "Function_2_3DC",          # 02, 2
        "Function_3_472",          # 03, 3
        "Function_4_5BA",          # 04, 4
        "Function_5_74B",          # 05, 5
        "Function_6_E7C",          # 06, 6
        "Function_7_1317",         # 07, 7
        "Function_8_18D0",         # 08, 8
        "Function_9_1A74",         # 09, 9
        "Function_10_1B0F",        # 0A, 10
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C8")
    Event(0, 7)
    Jump("loc_2DE")

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DA")
    Event(0, 6)
    Jump("loc_2DE")

    label("loc_2DA")

    Event(0, 5)

    label("loc_2DE")

    Return()

    # Function_0_2AE end

    def Function_1_2DF(): pass

    label("Function_1_2DF")

    OP_16(0x2, 0xFA0, 0xFFFD0260, 0xFFFF63C0, 0x230009)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x322, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303")
    OP_6F(0x0, 0)
    Jump("loc_30A")

    label("loc_303")

    OP_6F(0x0, 60)

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x322, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31C")
    OP_6F(0x1, 0)
    Jump("loc_323")

    label("loc_31C")

    OP_6F(0x1, 60)

    label("loc_323")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_35A")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)
    Jump("loc_3DB")

    label("loc_35A")

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_3DB")

    Return()

    # Function_1_2DF end

    def Function_2_3DC(): pass

    label("Function_2_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_471")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x28C58), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_40F")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_424")

    label("loc_40F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_424")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_424")

    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x28C58), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMUL), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_454")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469")

    label("loc_454")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_469")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_469")

    Sleep(10)
    Jump("Function_2_3DC")

    label("loc_471")

    Return()

    # Function_2_3DC end

    def Function_3_472(): pass

    label("Function_3_472")

    OP_EA(0x2, 0xBD, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x322, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_4E3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x00\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1910)
    Jump("loc_547")

    label("loc_4E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x00\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x00\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_547")

    Jump("loc_5AC")

    label("loc_54A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Oh, no, it's a Mimic! Prepare for battle!\x01",
            "...Wait. No? False alarm.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5AC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_472 end

    def Function_4_5BA(): pass

    label("Function_4_5BA")

    OP_EA(0x2, 0xBE, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x322, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_692")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x281, 1)"), scpexpr(EXPR_END)), "loc_62B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x81\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1911)
    Jump("loc_68F")

    label("loc_62B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x81\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x81\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_68F")

    Jump("loc_73D")

    label("loc_692")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Looking deep into the back of the chest, you\x01",
            "see a tiny, handwritten note that you didn't\x01",
            "notice previously. It reads, 'Please do not take.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_73D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5BA end

    def Function_5_74B(): pass

    label("Function_5_74B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_775")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_775")

    OP_6D(-34830, 1000, 170380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, -35500, 1000, 180520, 180)
    SetChrPos(0x103, -34500, 1000, 180520, 180)
    SetChrPos(0xF8, -35750, 1000, 181520, 180)
    SetChrPos(0xF9, -34250, 1000, 181520, 180)

    def lambda_801():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_801)
    Sleep(100)

    def lambda_821():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_821)
    Sleep(200)

    def lambda_841():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFDAE4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_841)
    Sleep(100)

    def lambda_861():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFDAE4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_861)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #6
        0x101,
        "#1004F#6PHey!\x02",
    )

    CloseMessageWindow()

    def lambda_89E():
        OP_8E(0xFE, 0xFFFF741E, 0x3E8, 0x27C9A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89E)
    Sleep(100)

    def lambda_8BE():
        OP_8E(0xFE, 0xFFFF7914, 0x3E8, 0x27C0E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8BE)
    Sleep(200)

    def lambda_8DE():
        OP_8E(0xFE, 0xFFFF73F6, 0x3E8, 0x282A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8DE)
    Sleep(100)

    def lambda_8FE():
        OP_8E(0xFE, 0xFFFF79B4, 0x3E8, 0x282DA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8FE)

    def lambda_919():
        OP_6D(-34940, 1000, 163860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_919)

    def lambda_931():
        OP_6B(3370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_931)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0x101, 180, 400)
    Sleep(50)
    OP_8C(0x103, 245, 400)
    Sleep(30)
    OP_8C(0xF8, 155, 400)
    Sleep(50)
    OP_8C(0xF9, 180, 400)
    Sleep(300)
    OP_8C(0x101, 180, 400)
    Sleep(50)
    OP_8C(0x103, 245, 400)
    Sleep(30)
    OP_8C(0xF8, 245, 400)
    Sleep(50)
    OP_8C(0xF9, 155, 400)
    Sleep(300)
    OP_8C(0x101, 245, 400)
    Sleep(50)
    OP_8C(0x103, 180, 400)
    Sleep(30)
    OP_8C(0xF8, 270, 400)
    Sleep(50)
    OP_8C(0xF9, 0, 400)
    Sleep(300)
    OP_8C(0x101, 0, 400)
    Sleep(50)
    OP_8C(0x103, 0, 400)
    Sleep(30)
    OP_8C(0xF8, 180, 400)
    Sleep(50)
    OP_8C(0xF9, 180, 400)
    Sleep(300)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A59")

    ChrTalk(    #7
        0x107,
        (
            "#560FWow! It's all bright\x01",
            "all of a sudden!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60")

    label("loc_A59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A97")

    ChrTalk(    #8
        0x106,
        "#051FHuh. Well, that's a lot less foggy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B60")

    label("loc_A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADE")

    ChrTalk(    #9
        0x104,
        (
            "#030FHm. The sun now shows her lovely\x01",
            "face to us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60")

    label("loc_ADE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2B")

    ChrTalk(    #10
        0x105,
        (
            "#048FHow wonderful.\x01",
            "The fog seems to have cleared here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B60")

    label("loc_B2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B60")

    ChrTalk(    #11
        0x108,
        "#070FHey, it's a lot brighter now.\x02",
    )

    CloseMessageWindow()

    label("loc_B60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC0")

    ChrTalk(    #12
        0x107,
        (
            "#061FI guess this is as far as the fog goes?\x01",
            "It kinda just...ends, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_BC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C28")

    ChrTalk(    #13
        0x106,
        (
            "#051FLooks like this is as far as it goes.\x01",
            "Sorta a quick end to the fog, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_C28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6F")

    ChrTalk(    #14
        0x104,
        "#030FIt seems the fog ends here...quite abruptly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_C6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCF")

    ChrTalk(    #15
        0x105,
        (
            "#048FThis seems to be as far as the fog goes.\x01",
            "It does end quickly, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_CCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D35")

    ChrTalk(    #16
        0x108,
        (
            "#070FGuess this is as far as the fog cover goes.\x01",
            "Kind of a sharp end to it, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D35")


    ChrTalk(    #17
        0x103,
        (
            "#026FSo along the Elize Highway, the fog clears\x01",
            "roughly 60 selge from the city.\x02\x03",

            "#020FThere don't seem to be any monsters in\x01",
            "the fog, either, so ensuring people's\x01",
            "safety shouldn't be difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#5P#1006FYeah, hopefully.\x02\x03",

            "I guess we should just check the other\x01",
            "roads like we did this one, then, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x180E)
    OP_28(0x8F, 0x2, 0x4)
    OP_28(0x8F, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_5_74B end

    def Function_6_E7C(): pass

    label("Function_6_E7C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EA6")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_EA6")

    OP_6D(-35370, 1000, 172190, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -35500, 1000, 172520, 180)
    SetChrPos(0x103, -34500, 1000, 172520, 180)
    SetChrPos(0xF8, -35750, 1000, 173520, 180)
    SetChrPos(0xF9, -34250, 1000, 173520, 180)

    def lambda_F2D():
        OP_8E(0xFE, 0xFFFF741E, 0x3E8, 0x27C9A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F2D)
    Sleep(100)

    def lambda_F4D():
        OP_8E(0xFE, 0xFFFF7914, 0x3E8, 0x27C0E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F4D)
    Sleep(200)

    def lambda_F6D():
        OP_8E(0xFE, 0xFFFF73F6, 0x3E8, 0x282A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_F6D)
    Sleep(100)

    def lambda_F8D():
        OP_8E(0xFE, 0xFFFF79B4, 0x3E8, 0x282DA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_F8D)

    def lambda_FA8():
        OP_6D(-34940, 1000, 163860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FA8)
    FadeToBright(1000, 0)
    OP_6B(3370, 3000)
    OP_0D()
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100C")

    ChrTalk(    #19
        0x107,
        "#061FYay, the fog's cleared! ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_10DE")

    label("loc_100C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103F")

    ChrTalk(    #20
        0x106,
        "#051FAnd we're outta the fog.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10DE")

    label("loc_103F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107A")

    ChrTalk(    #21
        0x104,
        "#030FAh, the fog ends here, it seems.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10DE")

    label("loc_107A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A9")

    ChrTalk(    #22
        0x105,
        "#048FThe fog has cleared.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10DE")

    label("loc_10A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DE")

    ChrTalk(    #23
        0x108,
        "#070FLooks like the fog's cleared.\x02",
    )

    CloseMessageWindow()

    label("loc_10DE")


    ChrTalk(    #24
        0x103,
        (
            "#026FSo along the Elize Highway, the fog clears\x01",
            "roughly sixty selge from the city.\x02\x03",

            "#020FThere don't seem to be any monsters in\x01",
            "the fog, either, so ensuring people's\x01",
            "safety shouldn't be difficult.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as investigated Malga Trail.\x01",           # 0
            "Set as investigated Milich Main Road.\x01",      # 1
            "No change\x01",                                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1248"),
        (1, "loc_1251"),
        (SWITCH_DEFAULT, "loc_125A"),
    )


    label("loc_1248")

    OP_A3(0x180F)
    OP_A2(0x1810)
    Jump("loc_125A")

    label("loc_1251")

    OP_A2(0x180F)
    OP_A3(0x1810)
    Jump("loc_125A")

    label("loc_125A")

    TurnDirection(0x101, 0x103, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_END)), "loc_12BA")

    ChrTalk(    #25
        0x101,
        (
            "#5P#1006FYeah, hopefully.\x02\x03",

            "Now we just need to check the\x01",
            "Milch Main Road.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1305")

    label("loc_12BA")


    ChrTalk(    #26
        0x101,
        (
            "#5P#1006FYeah, hopefully.\x02\x03",

            "Now we just need to check the\x01",
            "Malga Trail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1305")

    OP_A2(0x180E)
    OP_28(0x8F, 0x2, 0x4)
    OP_28(0x8F, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_6_E7C end

    def Function_7_1317(): pass

    label("Function_7_1317")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1341")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_1341")

    OP_6D(-35370, 1000, 172190, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -35500, 1000, 172520, 180)
    SetChrPos(0x103, -34500, 1000, 172520, 180)
    SetChrPos(0xF8, -35750, 1000, 173520, 180)
    SetChrPos(0xF9, -34250, 1000, 173520, 180)

    def lambda_13C8():
        OP_8E(0xFE, 0xFFFF741E, 0x3E8, 0x27C9A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13C8)
    Sleep(100)

    def lambda_13E8():
        OP_8E(0xFE, 0xFFFF7914, 0x3E8, 0x27C0E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13E8)
    Sleep(200)

    def lambda_1408():
        OP_8E(0xFE, 0xFFFF73F6, 0x3E8, 0x282A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1408)
    Sleep(100)

    def lambda_1428():
        OP_8E(0xFE, 0xFFFF79B4, 0x3E8, 0x282DA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1428)

    def lambda_1443():
        OP_6D(-34940, 1000, 163860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1443)
    FadeToBright(1000, 0)
    OP_6B(3370, 3000)
    OP_0D()
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A7")

    ChrTalk(    #27
        0x107,
        "#061FYay, the fog's cleared! ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_1579")

    label("loc_14A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DA")

    ChrTalk(    #28
        0x106,
        "#051FAnd we're outta the fog.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1579")

    label("loc_14DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1515")

    ChrTalk(    #29
        0x104,
        "#030FAh, the fog ends here, it seems.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1579")

    label("loc_1515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1544")

    ChrTalk(    #30
        0x105,
        "#048FThe fog has cleared.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1579")

    label("loc_1544")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1579")

    ChrTalk(    #31
        0x108,
        "#070FLooks like the fog's cleared.\x02",
    )

    CloseMessageWindow()

    label("loc_1579")


    ChrTalk(    #32
        0x103,
        (
            "#026FSo along the Elize Highway, the fog clears\x01",
            "roughly sixty selge from the city.\x02\x03",

            "#020FThere don't seem to be any monsters in\x01",
            "the fog, either, so ensuring people's\x01",
            "safety shouldn't be difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#5P#1006FYeah, hopefully.\x02\x03",

            "Well, that's all three roads\x01",
            "checked out, so...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #34
        0x101,
        (
            "#5P#1006FTime to head back and report\x01",
            "to Aina, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_177A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't visited Bright house\x01",      # 0
            "Set as visited Bright house\x01",              # 1
            "No change\x01",                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_176E"),
        (1, "loc_1774"),
        (SWITCH_DEFAULT, "loc_177A"),
    )


    label("loc_176E")

    OP_A3(0x180D)
    Jump("loc_177A")

    label("loc_1774")

    OP_A2(0x180D)
    Jump("loc_177A")

    label("loc_177A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1853")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #35
        0x103,
        (
            "#023F#4PWell, we can, \x02",

            "but didn't you want to go home\x01",
            "for a little while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#5P#1004FOh, yeah! I almost forgot.\x02\x03",

            "#1008FLet's stop by on our way back\x01",
            "to the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x2, 0x4)
    OP_28(0x8F, 0x1, 0x8)
    OP_28(0x8F, 0x1, 0x800)
    OP_28(0x8F, 0x1, 0x1000)
    Jump("loc_18CA")

    label("loc_1853")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #37
        0x103,
        (
            "#021F#4PUnless you can think of any other\x01",
            "pressing business, I'd say that's\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x2, 0x4)
    OP_28(0x8F, 0x1, 0x8)
    OP_28(0x8F, 0x1, 0x200)
    OP_28(0x8F, 0x1, 0x400)

    label("loc_18CA")

    OP_A2(0x180E)
    EventEnd(0x0)
    Return()

    # Function_7_1317 end

    def Function_8_18D0(): pass

    label("Function_8_18D0")

    EventBegin(0x1)

    ChrTalk(    #38
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_18FC():
        OP_6D(-93210, 980, 76900, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_18FC)

    def lambda_1914():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1914)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #39
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A64")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x6, 0xFFFE9B70, 0x3CA, 0x13312, 0xE1, 0xFFFE8BF8, 0x41A, 0x128E0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_1A5E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A58")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A55")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x10)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x05Recorded Elize Highway fishing spot in Bracer Notebook.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1A55")

    Jump("loc_1A5E")

    label("loc_1A58")

    OP_28(0x73, 0x1, 0x1000)

    label("loc_1A5E")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_1A73")

    label("loc_1A64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A73")
    EventEnd(0x1)

    label("loc_1A73")

    Return()

    # Function_8_18D0 end

    def Function_9_1A74(): pass

    label("Function_9_1A74")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_1AF0"),
        (1, "loc_1AF6"),
        (SWITCH_DEFAULT, "loc_1AFC"),
    )


    label("loc_1AF0")

    OP_A2(0x1200)
    Jump("loc_1AFC")

    label("loc_1AF6")

    OP_A2(0x1201)
    Jump("loc_1AFC")

    label("loc_1AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1B0A")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1B0E")

    label("loc_1B0A")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1B0E")

    Return()

    # Function_9_1A74 end

    def Function_10_1B0F(): pass

    label("Function_10_1B0F")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_10_1B0F end

    SaveToFile()

Try(main)
