from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7004   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7004.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60220",
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
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
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
        'ED6_DT29/CH14400 ._CH',             # 00
        'ED6_DT29/CH14401 ._CH',             # 01
        'ED6_DT29/CH14410 ._CH',             # 02
        'ED6_DT29/CH14411 ._CH',             # 03
        'ED6_DT29/CH14780 ._CH',             # 04
        'ED6_DT29/CH14781 ._CH',             # 05
        'ED6_DT29/CH14420 ._CH',             # 06
        'ED6_DT29/CH14421 ._CH',             # 07
        'ED6_DT29/CH14010 ._CH',             # 08
        'ED6_DT29/CH14011 ._CH',             # 09
        'ED6_DT29/CH14020 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT29/CH14400P._CP',             # 00
        'ED6_DT29/CH14401P._CP',             # 01
        'ED6_DT29/CH14410P._CP',             # 02
        'ED6_DT29/CH14411P._CP',             # 03
        'ED6_DT29/CH14780P._CP',             # 04
        'ED6_DT29/CH14781P._CP',             # 05
        'ED6_DT29/CH14420P._CP',             # 06
        'ED6_DT29/CH14421P._CP',             # 07
        'ED6_DT29/CH14010P._CP',             # 08
        'ED6_DT29/CH14011P._CP',             # 09
        'ED6_DT29/CH14020P._CP',             # 0A
    )

    DeclMonster(
        X                   = -37960,
        Z                   = 16000,
        Y                   = 1980,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35160,
        Z                   = 0,
        Y                   = -49150,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39980,
        Z                   = 0,
        Y                   = -53710,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30,
        Z                   = -4000,
        Y                   = -51990,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3220,
        Z                   = -20000,
        Y                   = -1170,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1320,
        Z                   = -20000,
        Y                   = 3150,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -37990,
        Z                   = -24000,
        Y                   = 1950,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34600,
        Z                   = -40000,
        Y                   = -48400,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39980,
        Z                   = -40000,
        Y                   = -53820,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40,
        Z                   = -44000,
        Y                   = -52050,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4390,
        Z                   = -60000,
        Y                   = -2420,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4390,
        Z                   = -60000,
        Y                   = 6300,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4310,
        Z                   = -60000,
        Y                   = 6300,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4310,
        Z                   = -60000,
        Y                   = -2270,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -2730,
        Y                   = -60800,
        Z                   = 16000,
        Range               = 2790,
        Unknown_10          = 0xFFFF2928,
        Unknown_14          = 0x4CFE,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = -39860,
        TriggerZ            = 0,
        TriggerY            = -55290,
        TriggerRange        = 1000,
        ActorX              = -40000,
        ActorZ              = 1000,
        ActorY              = -56000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -35860,
        TriggerZ            = 0,
        TriggerY            = -55290,
        TriggerRange        = 1000,
        ActorX              = -36000,
        ActorZ              = 1000,
        ActorY              = -56000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2F2",          # 00, 0
        "Function_1_31D",          # 01, 1
        "Function_2_389",          # 02, 2
        "Function_3_4D0",          # 03, 3
        "Function_4_5D5",          # 04, 4
        "Function_5_6DC",          # 05, 5
        "Function_6_8CF",          # 06, 6
        "Function_7_9AD",          # 07, 7
        "Function_8_A69",          # 08, 8
        "Function_9_B7F",          # 09, 9
    )


    def Function_0_2F2(): pass

    label("Function_0_2F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_30E"),
        (101, "loc_315"),
        (SWITCH_DEFAULT, "loc_31C"),
    )


    label("loc_30E")

    Event(0, 6)
    Jump("loc_31C")

    label("loc_315")

    Event(0, 5)
    Jump("loc_31C")

    label("loc_31C")

    Return()

    # Function_0_2F2 end

    def Function_1_31D(): pass

    label("Function_1_31D")

    OP_16(0x2, 0xFA0, 0xFFFDBBEC, 0xFFFDA576, 0x230080)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_1B(0x0, 0x0, 0x7)

    label("loc_340")

    OP_10(0x1, 0x0)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368")
    OP_6F(0x1, 0)
    Jump("loc_36F")

    label("loc_368")

    OP_6F(0x1, 60)

    label("loc_36F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381")
    OP_6F(0x2, 0)
    Jump("loc_388")

    label("loc_381")

    OP_6F(0x2, 60)

    label("loc_388")

    Return()

    # Function_1_31D end

    def Function_2_389(): pass

    label("Function_2_389")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_462")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1B5, 1)"), scpexpr(EXPR_END)), "loc_3F7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xB5\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x269C)
    Jump("loc_45F")

    label("loc_3F7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xB5\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xB5\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_45F")

    Jump("loc_4C2")

    label("loc_462")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05I really should have ordered that security orbment from ZCF.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xAC, 0x0)

    label("loc_4C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_389 end

    def Function_3_4D0(): pass

    label("Function_3_4D0")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_577")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 0x32)
    AddSepith(0x5, 0x32)
    AddSepith(0x6, 0x32)

    AnonymousTalk(    #3
        (
            "\x07\x02Obtained:\x01",
            "#62ITime Sepith x50\x01",
            "#60ISpace Sepith x50\x01",
            "#61IMirage Sepith x50.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x269D)
    Jump("loc_5BE")

    label("loc_577")


    AnonymousTalk(    #4
        (
            "\x07\x05A forgotten chest\x01",
            "Despoiled and left behind\x01",
            "Its sad lot in life\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5BE")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xAD, 0x0)
    Return()

    # Function_3_4D0 end

    def Function_4_5D5(): pass

    label("Function_4_5D5")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-70, -60050, 18050, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 0, -60000, 19000, 0)
    OP_89(0x1, 1000, -60000, 18000, 0)
    OP_89(0x2, -1000, -60000, 18000, 0)
    OP_89(0x3, 0, -60000, 17150, 0)
    OP_0D()
    Sleep(300)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_B0(0x0, 0x28)
    OP_6F(0x0, 0)
    OP_70(0x0, 0xE6)

    def lambda_685():
        OP_6D(-70, -99000, 18050, 9000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_685)

    def lambda_69D():
        OP_67(0, 8500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_69D)

    def lambda_6B5():
        OP_6C(57000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6B5)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7006   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_5D5 end

    def Function_5_6DC(): pass

    label("Function_5_6DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6F(0x0, 180)
    OP_70(0x0, 0xB4)
    OP_48()
    OP_6D(-40, -70450, 17720, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(4580, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 0, -88000, 17290, 180)
    OP_89(0x1, -1000, -88000, 18190, 180)
    OP_89(0x2, 1000, -88000, 18190, 180)
    OP_89(0x3, 0, -88000, 19180, 180)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_B0(0x0, 0x28)
    OP_6F(0x0, 180)
    OP_70(0x0, 0x0)

    def lambda_79A():
        OP_6D(-70, -60050, 18050, 4500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_79A)

    def lambda_7B2():
        OP_67(0, 8500, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7B2)

    def lambda_7CA():
        OP_6B(3400, 4500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7CA)

    def lambda_7DA():
        OP_6C(45000, 4500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_7DA)
    FadeToBright(1000, 0)
    Sleep(2200)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x0, 0x0)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 80, -60000, 13970, 180)
    SetChrPos(0x1, 80, -60000, 13970, 180)
    SetChrPos(0x2, 80, -60000, 13970, 180)
    SetChrPos(0x3, 80, -60000, 13970, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_5_6DC end

    def Function_6_8CF(): pass

    label("Function_6_8CF")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -820, 20000, 1840, 270)
    SetChrPos(0x1, -40, 20000, 2890, 270)
    SetChrPos(0x2, -100, 20000, 1110, 270)
    SetChrPos(0x3, 820, 20000, 2040, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 20000, 2100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 8)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_6_8CF end

    def Function_7_9AD(): pass

    label("Function_7_9AD")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -920, 20000, 1870, 90)
    SetChrPos(0x2, -40, 20000, 2890, 90)
    SetChrPos(0x1, -100, 20000, 1110, 90)
    SetChrPos(0x0, 820, 20000, 2040, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 20000, 2100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 9)
    NewScene("ED6_DT21/M7003   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_7_9AD end

    def Function_8_A69(): pass

    label("Function_8_A69")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A92")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_A86():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A86)

    label("loc_A92")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABB")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AAF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AAF)

    label("loc_ABB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AE4")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AD8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AD8)

    label("loc_AE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0D")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_B01():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B01)

    label("loc_B0D")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B39")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_B39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B50")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_B50")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B67")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_B67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7E")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_B7E")

    Return()

    # Function_8_A69 end

    def Function_9_B7F(): pass

    label("Function_9_B7F")


    def lambda_B85():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B85)

    def lambda_B97():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B97)

    def lambda_BA9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_BA9)

    def lambda_BBB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_BBB)
    Sleep(1000)
    Return()

    # Function_9_B7F end

    SaveToFile()

Try(main)
