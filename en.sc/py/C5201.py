from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5201   ._SN',
        MapName             = 'Other',
        Location            = 'C5201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60063",
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
        'Phenomenon',                           # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12950 ._CH',             # 00
        'ED6_DT29/CH12951 ._CH',             # 01
        'ED6_DT29/CH12000 ._CH',             # 02
        'ED6_DT29/CH12001 ._CH',             # 03
        'ED6_DT29/CH12960 ._CH',             # 04
        'ED6_DT29/CH12961 ._CH',             # 05
        'ED6_DT29/CH12962 ._CH',             # 06
        'ED6_DT27/CH04000 ._CH',             # 07
        'ED6_DT27/CH04010 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT29/CH12950P._CP',             # 00
        'ED6_DT29/CH12951P._CP',             # 01
        'ED6_DT29/CH12000P._CP',             # 02
        'ED6_DT29/CH12001P._CP',             # 03
        'ED6_DT29/CH12960P._CP',             # 04
        'ED6_DT29/CH12961P._CP',             # 05
        'ED6_DT29/CH12962P._CP',             # 06
        'ED6_DT27/CH04000P._CP',             # 07
        'ED6_DT27/CH04010P._CP',             # 08
    )

    DeclNpc(
        X                   = 12860,
        Z                   = 6000,
        Y                   = -184960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -97710,
        Z                   = 0,
        Y                   = 64019,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34000,
        Z                   = 0,
        Y                   = -185250,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 126250,
        Z                   = 4000,
        Y                   = -186970,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 136370,
        Z                   = 4000,
        Y                   = -203580,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -1220,
        Y                   = 0,
        Z                   = -181040,
        Range               = 2840,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFD12E6,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = -50270,
        TriggerZ            = 0,
        TriggerY            = 52050,
        TriggerRange        = 1000,
        ActorX              = -49650,
        ActorZ              = 0,
        ActorY              = 52050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -50090,
        TriggerZ            = 0,
        TriggerY            = 16090,
        TriggerRange        = 1000,
        ActorX              = -49470,
        ActorZ              = 0,
        ActorY              = 16090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_209",          # 01, 1
        "Function_2_240",          # 02, 2
        "Function_3_256",          # 03, 3
        "Function_4_379",          # 04, 4
        "Function_5_629",          # 05, 5
        "Function_6_704",          # 06, 6
        "Function_7_7E8",          # 07, 7
        "Function_8_946",          # 08, 8
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208")
    SetChrPos(0x8, 12860, 6000, -184960, 270)
    ClearChrFlags(0x8, 0x80)

    label("loc_208")

    Return()

    # Function_0_1EA end

    def Function_1_209(): pass

    label("Function_1_209")

    Call(0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F")
    OP_6F(0x8, 0)
    Jump("loc_226")

    label("loc_21F")

    OP_6F(0x8, 60)

    label("loc_226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238")
    OP_6F(0x9, 0)
    Jump("loc_23F")

    label("loc_238")

    OP_6F(0x9, 60)

    label("loc_23F")

    Return()

    # Function_1_209 end

    def Function_2_240(): pass

    label("Function_2_240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_255")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_240")

    label("loc_255")

    Return()

    # Function_2_240 end

    def Function_3_256(): pass

    label("Function_3_256")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_27F"),
        (3, "loc_28C"),
        (4, "loc_299"),
        (5, "loc_2A6"),
        (6, "loc_2B3"),
        (7, "loc_2C0"),
        (8, "loc_2CD"),
        (10, "loc_2DA"),
        (SWITCH_DEFAULT, "loc_2E7"),
    )


    label("loc_27F")

    OP_D2(0x701D0, 0x701DC, 0x9)
    Jump("loc_2E7")

    label("loc_28C")

    OP_D2(0x701E8, 0x701F4, 0x9)
    Jump("loc_2E7")

    label("loc_299")

    OP_D2(0x27036E, 0x27037B, 0x9)
    Jump("loc_2E7")

    label("loc_2A6")

    OP_D2(0x70218, 0x70224, 0x9)
    Jump("loc_2E7")

    label("loc_2B3")

    OP_D2(0x70230, 0x7023C, 0x9)
    Jump("loc_2E7")

    label("loc_2C0")

    OP_D2(0x70248, 0x70254, 0x9)
    Jump("loc_2E7")

    label("loc_2CD")

    OP_D2(0x270176, 0x270183, 0x9)
    Jump("loc_2E7")

    label("loc_2DA")

    OP_D2(0x702B4, 0x702BB, 0x9)
    Jump("loc_2E7")

    label("loc_2E7")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_310"),
        (3, "loc_31D"),
        (4, "loc_32A"),
        (5, "loc_337"),
        (6, "loc_344"),
        (7, "loc_351"),
        (8, "loc_35E"),
        (10, "loc_36B"),
        (SWITCH_DEFAULT, "loc_378"),
    )


    label("loc_310")

    OP_D2(0x701D0, 0x701DC, 0xA)
    Jump("loc_378")

    label("loc_31D")

    OP_D2(0x701E8, 0x701F4, 0xA)
    Jump("loc_378")

    label("loc_32A")

    OP_D2(0x27036E, 0x27037B, 0xA)
    Jump("loc_378")

    label("loc_337")

    OP_D2(0x70218, 0x70224, 0xA)
    Jump("loc_378")

    label("loc_344")

    OP_D2(0x70230, 0x7023C, 0xA)
    Jump("loc_378")

    label("loc_351")

    OP_D2(0x70248, 0x70254, 0xA)
    Jump("loc_378")

    label("loc_35E")

    OP_D2(0x270176, 0x270183, 0xA)
    Jump("loc_378")

    label("loc_36B")

    OP_D2(0x702B4, 0x702BB, 0xA)
    Jump("loc_378")

    label("loc_378")

    Return()

    # Function_3_256 end

    def Function_4_379(): pass

    label("Function_4_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 7)), scpexpr(EXPR_END)), "loc_381")
    Return()

    label("loc_381")

    EventBegin(0x0)
    Fade(500)
    OP_6D(2460, 0, -184440, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(65000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 12860, 6000, -184960, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -430, 0, -185160, 90)
    SetChrPos(0x102, -1300, 0, -184290, 90)
    SetChrPos(0xF8, -2510, 0, -185420, 90)
    SetChrPos(0xF9, -2100, 0, -186450, 90)

    def lambda_425():
        OP_91(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_425)

    def lambda_440():
        OP_91(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_440)

    def lambda_45B():
        OP_91(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_45B)

    def lambda_476():
        OP_91(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_476)

    def lambda_491():
        OP_6D(6460, 0, -184440, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_491)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 3)

    def lambda_4B9():
        OP_96(0xFE, 0x229C, 0x0, 0xFFFD2D80, 0x64, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4B9)
    OP_22(0xA3, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 7)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 8)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 9)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 10)
    SetChrSubChip(0xF9, 0)

    def lambda_579():
        OP_99(0xFE, 0x3, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_579)
    WaitChrThread(0x8, 0x2)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Sleep(1500)
    OP_44(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)

    def lambda_5AD():
        OP_99(0xFE, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5AD)
    WaitChrThread(0x8, 0x2)

    def lambda_5C2():
        OP_99(0xFE, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5C2)

    def lambda_5D2():
        OP_96(0xFE, 0x9A6, 0x0, 0xFFFD2CB8, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D2)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(500)
    Battle(0x43E, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_615"),
        (0, "loc_61A"),
        (2, "loc_621"),
        (SWITCH_DEFAULT, "loc_628"),
    )


    label("loc_615")

    OP_B4(0x0)
    Jump("loc_628")

    label("loc_61A")

    Call(0, 5)
    Jump("loc_628")

    label("loc_621")

    Call(0, 6)
    Jump("loc_628")

    label("loc_628")

    Return()

    # Function_4_379 end

    def Function_5_629(): pass

    label("Function_5_629")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    SetChrFlags(0x8, 0x80)
    OP_6D(1420, 0, -185200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1420, 0, -185200, 90)
    SetChrPos(0x1, 1420, 0, -185200, 90)
    SetChrPos(0x2, 1420, 0, -185200, 90)
    SetChrPos(0x3, 1420, 0, -185200, 90)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x22FF)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_629 end

    def Function_6_704(): pass

    label("Function_6_704")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    SetChrPos(0x8, 12860, 6000, -184960, 270)
    ClearChrFlags(0x8, 0x80)
    OP_6D(-3750, 0, -185200, 270)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -3750, 0, -185200, 270)
    SetChrPos(0x1, -3750, 0, -185200, 270)
    SetChrPos(0x2, -3750, 0, -185200, 270)
    SetChrPos(0x3, -3750, 0, -185200, 270)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_704 end

    def Function_7_7E8(): pass

    label("Function_7_7E8")

    OP_EA(0x2, 0x10, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_859")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x05\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2309)
    Jump("loc_8BD")

    label("loc_859")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x05\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x05\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_8BD")

    Jump("loc_938")

    label("loc_8C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You can save the world, but you can't remember\x01",
            "whether you've looted a chest once or not?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_938")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_7E8 end

    def Function_8_946(): pass

    label("Function_8_946")

    OP_EA(0x2, 0x11, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x461, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_9B7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x230A)
    Jump("loc_A1B")

    label("loc_9B7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_A1B")

    Jump("loc_A82")

    label("loc_A1E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05It's empty, but if you put your head in here, you\x01",
            "can hear the ocean!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A82")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_946 end

    SaveToFile()

Try(main)
