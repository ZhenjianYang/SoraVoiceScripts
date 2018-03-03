from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4138   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4138.x',
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
        'Dark Blade',                           # 9
        'Dark Blade',                           # 10
        'Dark Blade',                           # 11
        'Dark Blade',                           # 12
        'Sealing Stone 3',                      # 13
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
        'ED6_DT29/CH14520 ._CH',             # 00
        'ED6_DT29/CH14521 ._CH',             # 01
        'ED6_DT27/CH04080 ._CH',             # 02
        'ED6_DT27/CH04150 ._CH',             # 03
        'ED6_DT07/CH00160 ._CH',             # 04
        'ED6_DT27/CH04580 ._CH',             # 05
        'ED6_DT26/CH20621 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT29/CH14520P._CP',             # 00
        'ED6_DT29/CH14521P._CP',             # 01
        'ED6_DT27/CH04080P._CP',             # 02
        'ED6_DT27/CH04150P._CP',             # 03
        'ED6_DT07/CH00160P._CP',             # 04
        'ED6_DT27/CH04580P._CP',             # 05
        'ED6_DT26/CH20621P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
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
        TriggerX            = -49190,
        TriggerZ            = 1000,
        TriggerY            = 63810,
        TriggerRange        = 1000,
        ActorX              = -49190,
        ActorZ              = 2000,
        ActorY              = 63810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = 76130,
        TriggerRange        = 1000,
        ActorX              = 4970,
        ActorZ              = 1000,
        ActorY              = 76130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54740,
        TriggerZ            = 0,
        TriggerY            = 65190,
        TriggerRange        = 1000,
        ActorX              = 54740,
        ActorZ              = 1000,
        ActorY              = 65190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EE",          # 00, 0
        "Function_1_21C",          # 01, 1
        "Function_2_32B",          # 02, 2
        "Function_3_861",          # 03, 3
        "Function_4_885",          # 04, 4
        "Function_5_8AE",          # 05, 5
        "Function_6_8E9",          # 06, 6
        "Function_7_912",          # 07, 7
        "Function_8_9B5",          # 08, 8
        "Function_9_A58",          # 09, 9
        "Function_10_AFB",         # 0A, 10
        "Function_11_B9E",         # 0B, 11
        "Function_12_1024",        # 0C, 12
        "Function_13_13E3",        # 0D, 13
        "Function_14_151D",        # 0E, 14
    )


    def Function_0_1EE(): pass

    label("Function_0_1EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206")
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_21B")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_21B")

    Return()

    # Function_0_1EE end

    def Function_1_21C(): pass

    label("Function_1_21C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_22F")
    OP_B1("U4138_y")
    Jump("loc_238")

    label("loc_22F")

    OP_B1("U4138_n")

    label("loc_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4")
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, -49000, 2100, 63810, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_2F8")

    label("loc_2F4")

    OP_64(0x0, 0x1)

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A")
    OP_6F(0x5, 0)
    Jump("loc_311")

    label("loc_30A")

    OP_6F(0x5, 60)

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323")
    OP_6F(0x6, 0)
    Jump("loc_32A")

    label("loc_323")

    OP_6F(0x6, 60)

    label("loc_32A")

    Return()

    # Function_1_21C end

    def Function_2_32B(): pass

    label("Function_2_32B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A2(0x2705)
    LoadEffect(0x1, "map\\mp250_01.eff")
    SetChrPos(0x109, 140, 0, 630, 0)
    SetChrPos(0x10F, 1260, 0, 70, 0)
    SetChrPos(0x107, -170, 0, -930, 0)
    SetChrPos(0x10E, 1320, 0, -1310, 0)
    OP_6D(1510, 5500, 7940, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(45000, 0)
    OP_6E(340, 0)

    def lambda_3D4():
        OP_6D(1510, 0, 7940, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D4)

    def lambda_3EC():
        OP_67(0, 6130, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3EC)

    def lambda_404():
        OP_6B(2480, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_404)

    def lambda_414():
        OP_6E(362, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_414)

    def lambda_424():
        OP_8E(0xFE, 0xA0, 0x0, 0x1CA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_424)
    Sleep(100)

    def lambda_444():
        OP_8E(0xFE, 0x56E, 0x0, 0x1B62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_444)
    Sleep(100)

    def lambda_464():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x1720, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_464)
    Sleep(100)

    def lambda_484():
        OP_8E(0xFE, 0x46A, 0x0, 0x15CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_484)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)
    OP_20(0x3E8)

    def lambda_4CC():
        OP_6B(2600, 1300)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_4CC)
    OP_43(0x10, 0x0, 0x0, 0x7)
    Sleep(100)
    OP_43(0x11, 0x0, 0x0, 0x8)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x9)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0x107, 0x0, 0x0, 0x5)
    OP_43(0x10E, 0x0, 0x0, 0x6)
    WaitChrThread(0x13, 0x0)
    OP_1D(0x97)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1441F#6P...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #1
        0x109,
        "#1069F#6PNo time to get comfy, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x107,
        "#065F#5PThey just popped up out of nowhere!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 4)
    SetChrSubChip(0x107, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 5)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #3
        0x10E,
        "#177F#6PHere they come!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_63B():
        OP_6D(1730, 0, 7710, 200)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_63B)

    def lambda_653():
        OP_6B(1900, 200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_653)

    def lambda_663():

        label("loc_663")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_663")

    QueueWorkItem2(0x10, 3, lambda_663)
    SetChrChipByIndex(0x10, 1)

    def lambda_67B():
        OP_8F(0xFE, 0xFFFFF79A, 0x0, 0x15B8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_67B)
    Sleep(20)

    def lambda_69B():

        label("loc_69B")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_69B")

    QueueWorkItem2(0x12, 3, lambda_69B)
    SetChrChipByIndex(0x12, 1)

    def lambda_6B3():
        OP_8F(0xFE, 0x848, 0x0, 0x2076, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6B3)
    Sleep(20)

    def lambda_6D3():

        label("loc_6D3")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_6D3")

    QueueWorkItem2(0x13, 3, lambda_6D3)
    SetChrChipByIndex(0x13, 1)

    def lambda_6EB():
        OP_8F(0xFE, 0xA78, 0x0, 0x1608, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6EB)
    Sleep(30)

    def lambda_70B():

        label("loc_70B")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_70B")

    QueueWorkItem2(0x11, 3, lambda_70B)
    SetChrChipByIndex(0x11, 1)

    def lambda_723():
        OP_8F(0xFE, 0xFFFFFE8E, 0x0, 0x2242, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_723)
    WaitChrThread(0x109, 0x0)
    Battle(0xF1, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_768"),
        (2, "loc_84D"),
        (1, "loc_859"),
        (SWITCH_DEFAULT, "loc_85E"),
    )


    label("loc_768")

    EventBegin(0x0)
    OP_6D(810, 0, 5780, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x0, 810, 0, 5780, 0)
    SetChrPos(0x1, 810, 0, 5780, 0)
    SetChrPos(0x2, 810, 0, 5780, 0)
    SetChrPos(0x3, 810, 0, 5780, 0)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    OP_A2(0x2706)
    FadeToBright(1000, 0)
    Jump("loc_85E")

    label("loc_84D")

    NewScene("ED6_DT21/U4101   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_85E")

    label("loc_859")

    OP_B4(0x0)
    Jump("loc_85E")

    label("loc_85E")

    EventEnd(0x0)
    Return()

    # Function_2_32B end

    def Function_3_861(): pass

    label("Function_3_861")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1300)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_861 end

    def Function_4_885(): pass

    label("Function_4_885")

    Sleep(50)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_4_885 end

    def Function_5_8AE(): pass

    label("Function_5_8AE")

    Sleep(100)
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1100)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_5_8AE end

    def Function_6_8E9(): pass

    label("Function_6_8E9")

    Sleep(150)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_8E9 end

    def Function_7_912(): pass

    label("Function_7_912")

    SetChrPos(0xFE, -4780, 0, 5780, 90)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_939():

        label("loc_939")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_939")

    QueueWorkItem2(0xFE, 3, lambda_939)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x800)
    PlayEffect(0x1, 0x0, 0xFE, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_99B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99B)
    OP_82(0x0, 0x2)
    Sleep(300)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_7_912 end

    def Function_8_9B5(): pass

    label("Function_8_9B5")

    SetChrPos(0xFE, -1530, 0, 11320, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9DC():

        label("loc_9DC")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_9DC")

    QueueWorkItem2(0xFE, 3, lambda_9DC)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x800)
    PlayEffect(0x1, 0x1, 0xFE, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_A3E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3E)
    OP_82(0x1, 0x2)
    Sleep(300)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_8_9B5 end

    def Function_9_A58(): pass

    label("Function_9_A58")

    SetChrPos(0xFE, 3480, 0, 10830, 225)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A7F():

        label("loc_A7F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A7F")

    QueueWorkItem2(0xFE, 3, lambda_A7F)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x800)
    PlayEffect(0x1, 0x2, 0xFE, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_AE1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE1)
    OP_82(0x2, 0x2)
    Sleep(300)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_9_A58 end

    def Function_10_AFB(): pass

    label("Function_10_AFB")

    SetChrPos(0xFE, 6000, 0, 5870, 270)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_B22():

        label("loc_B22")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B22")

    QueueWorkItem2(0xFE, 3, lambda_B22)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x800)
    PlayEffect(0x1, 0x3, 0xFE, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_B84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B84)
    OP_82(0x3, 0x2)
    Sleep(300)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_10_AFB end

    def Function_11_B9E(): pass

    label("Function_11_B9E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x1, "map\\mp250_01.eff")
    SetChrPos(0x109, 140, 0, 630, 0)
    SetChrPos(0x10F, 1260, 0, 70, 0)
    SetChrPos(0x107, -170, 0, -930, 0)
    SetChrPos(0x10E, 1320, 0, -1310, 0)
    OP_6D(1510, 5500, 7940, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(45000, 0)
    OP_6E(340, 0)

    def lambda_C44():
        OP_6D(1510, 0, 7940, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C44)

    def lambda_C5C():
        OP_67(0, 6130, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C5C)

    def lambda_C74():
        OP_6B(2480, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_C74)

    def lambda_C84():
        OP_6E(362, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C84)

    def lambda_C94():
        OP_8E(0xFE, 0xA0, 0x0, 0x1CA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C94)
    Sleep(100)

    def lambda_CB4():
        OP_8E(0xFE, 0x56E, 0x0, 0x1B62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_CB4)
    Sleep(100)

    def lambda_CD4():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x1720, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_CD4)
    Sleep(100)

    def lambda_CF4():
        OP_8E(0xFE, 0x46A, 0x0, 0x15CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_CF4)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)
    OP_20(0x3E8)

    def lambda_D3C():
        OP_6B(2600, 1300)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_D3C)
    OP_43(0x10, 0x0, 0x0, 0x7)
    Sleep(100)
    OP_43(0x11, 0x0, 0x0, 0x8)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x9)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0xA)
    WaitChrThread(0x13, 0x0)

    def lambda_D7C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_D7C)
    Sleep(100)
    OP_8C(0x10E, 90, 400)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 4)
    SetChrSubChip(0x107, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 5)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_DF5():
        OP_6D(1730, 0, 7710, 200)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DF5)

    def lambda_E0D():
        OP_6B(1900, 200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E0D)

    def lambda_E1D():

        label("loc_E1D")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_E1D")

    QueueWorkItem2(0x10, 3, lambda_E1D)
    SetChrChipByIndex(0x10, 1)

    def lambda_E35():
        OP_8F(0xFE, 0xFFFFF79A, 0x0, 0x15B8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_E35)
    Sleep(20)

    def lambda_E55():

        label("loc_E55")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_E55")

    QueueWorkItem2(0x12, 3, lambda_E55)
    SetChrChipByIndex(0x12, 1)

    def lambda_E6D():
        OP_8F(0xFE, 0x848, 0x0, 0x2076, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_E6D)
    Sleep(20)

    def lambda_E8D():

        label("loc_E8D")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_E8D")

    QueueWorkItem2(0x13, 3, lambda_E8D)
    SetChrChipByIndex(0x13, 1)

    def lambda_EA5():
        OP_8F(0xFE, 0xA78, 0x0, 0x1608, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_EA5)
    Sleep(30)

    def lambda_EC5():

        label("loc_EC5")

        OP_99(0xFE, 0x0, 0x6, 0x3E8)
        OP_48()
        Jump("loc_EC5")

    QueueWorkItem2(0x11, 3, lambda_EC5)
    SetChrChipByIndex(0x11, 1)

    def lambda_EDD():
        OP_8F(0xFE, 0xFFFFFE8E, 0x0, 0x2242, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_EDD)
    WaitChrThread(0x109, 0x0)
    Battle(0xF1, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F22"),
        (2, "loc_1010"),
        (1, "loc_101C"),
        (SWITCH_DEFAULT, "loc_1021"),
    )


    label("loc_F22")

    EventBegin(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(810, 0, 5780, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x0, 810, 0, 5780, 0)
    SetChrPos(0x1, 810, 0, 5780, 0)
    SetChrPos(0x2, 810, 0, 5780, 0)
    SetChrPos(0x3, 810, 0, 5780, 0)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    OP_A2(0x2706)
    FadeToBright(1000, 0)
    Jump("loc_1021")

    label("loc_1010")

    NewScene("ED6_DT21/U4101   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_1021")

    label("loc_101C")

    OP_B4(0x0)
    Jump("loc_1021")

    label("loc_1021")

    EventEnd(0x0)
    Return()

    # Function_11_B9E end

    def Function_12_1024(): pass

    label("Function_12_1024")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -49390, 1000, 62530, 0)
    SetChrPos(0x10F, -47550, 1000, 63700, 270)
    SetChrPos(0x107, -50770, 1000, 62130, 45)
    SetChrPos(0x10E, -51210, 1000, 63420, 90)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    OP_6D(-48350, 1000, 64590, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 6)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x14, 0xFFFF4034, 0x898, 0xF64A, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x14, 0x80)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05Obtained \x1F\x54\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x354, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #5
        0x10E,
        "#173F#6PIs that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1448F#2PIndeed. We found you and Tita inside\x01",
            "stones just like this.\x02\x03",

            "At this point, it's safe to assume there's\x01",
            "someone sealed inside this one, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x107,
        (
            "#062F#6PWell, it's in the Erebonian embassy,\x01",
            "so maybe it's Olivier?\x02\x03",

            "#064F...Oh, wait. Joshua was born in Erebonia,\x01",
            "too, wasn't he? Hmm...\x02\x03",

            "#067FI don't care who it is! I can't wait to find\x01",
            "out who's inside!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #8
        0x109,
        (
            "#1075F#2PWell, there's only one way to know for sure.\x02\x03",

            "#1060FThere's no rush, but we should try and make\x01",
            "our way back to the base soon and check for\x01",
            "ourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2707)
    OP_28(0x2B, 0x1, 0x40)
    OP_28(0x2B, 0x1, 0x80)
    OP_64(0x0, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_1024 end

    def Function_13_13E3(): pass

    label("Function_13_13E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x611, 1)"), scpexpr(EXPR_END)), "loc_1451")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x11\x06\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27BE)
    Jump("loc_14B9")

    label("loc_1451")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x11\x06\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x11\x06\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_14B9")

    Jump("loc_150F")

    label("loc_14BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05I'm empty, you say? What a Liberlous statement!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x114, 0x0)

    label("loc_150F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_13E3 end

    def Function_14_151D(): pass

    label("Function_14_151D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_158B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Found \x1F\xF6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27BF)
    Jump("loc_15F3")

    label("loc_158B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Found \x1F\xF6\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF6\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_15F3")

    Jump("loc_1636")

    label("loc_15F6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05You are the *real* treasure.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x115, 0x0)

    label("loc_1636")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_151D end

    SaveToFile()

Try(main)
