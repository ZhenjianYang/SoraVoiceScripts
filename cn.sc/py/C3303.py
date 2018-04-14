from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3303   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3303.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3303_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '吉米',                                 # 9
        '妖化企鹅',                             # 10
        '企鹅',                                 # 11
        '企鹅',                                 # 12
        '小企鹅',                               # 13
        '企鹅',                                 # 14
        '企鹅',                                 # 15
        '小企鹅',                               # 16
        '回音',                                 # 17
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT29/CH12930 ._CH',             # 01
        'ED6_DT09/CH10630 ._CH',             # 02
        'ED6_DT09/CH10640 ._CH',             # 03
        'ED6_DT09/CH10650 ._CH',             # 04
        'ED6_DT09/CH10660 ._CH',             # 05
        'ED6_DT09/CH10670 ._CH',             # 06
        'ED6_DT09/CH10690 ._CH',             # 07
        'ED6_DT27/CH04000 ._CH',             # 08
        'ED6_DT27/CH04001 ._CH',             # 09
        'ED6_DT07/CH00120 ._CH',             # 0A
        'ED6_DT07/CH00121 ._CH',             # 0B
        'ED6_DT06/CH20137 ._CH',             # 0C
        'ED6_DT07/CH00151 ._CH',             # 0D
        'ED6_DT07/CH00130 ._CH',             # 0E
        'ED6_DT07/CH00131 ._CH',             # 0F
        'ED6_DT07/CH00140 ._CH',             # 10
        'ED6_DT07/CH00141 ._CH',             # 11
        'ED6_DT07/CH00160 ._CH',             # 12
        'ED6_DT07/CH00161 ._CH',             # 13
        'ED6_DT07/CH00170 ._CH',             # 14
        'ED6_DT07/CH00171 ._CH',             # 15
        'ED6_DT27/CH03005 ._CH',             # 16
        'ED6_DT26/CH20311 ._CH',             # 17
        'ED6_DT29/CH12932 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT29/CH12930P._CP',             # 01
        'ED6_DT09/CH10630P._CP',             # 02
        'ED6_DT09/CH10640P._CP',             # 03
        'ED6_DT09/CH10650P._CP',             # 04
        'ED6_DT09/CH10660P._CP',             # 05
        'ED6_DT09/CH10670P._CP',             # 06
        'ED6_DT09/CH10690P._CP',             # 07
        'ED6_DT27/CH04000P._CP',             # 08
        'ED6_DT27/CH04001P._CP',             # 09
        'ED6_DT07/CH00120P._CP',             # 0A
        'ED6_DT07/CH00121P._CP',             # 0B
        'ED6_DT06/CH20137P._CP',             # 0C
        'ED6_DT07/CH00151P._CP',             # 0D
        'ED6_DT07/CH00130P._CP',             # 0E
        'ED6_DT07/CH00131P._CP',             # 0F
        'ED6_DT07/CH00140P._CP',             # 10
        'ED6_DT07/CH00141P._CP',             # 11
        'ED6_DT07/CH00160P._CP',             # 12
        'ED6_DT07/CH00161P._CP',             # 13
        'ED6_DT07/CH00170P._CP',             # 14
        'ED6_DT07/CH00171P._CP',             # 15
        'ED6_DT27/CH03005P._CP',             # 16
        'ED6_DT26/CH20311P._CP',             # 17
        'ED6_DT29/CH12932P._CP',             # 18
    )

    DeclNpc(
        X                   = 9460,
        Z                   = 40,
        Y                   = 112430,
        Direction           = 90,
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
        X                   = 8000,
        Z                   = -3500,
        Y                   = 119800,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 12660,
        Y                   = -2000,
        Z                   = 95880,
        Range               = 3560,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1848E,
        Unknown_18          = 0x10000,
        Unknown_1C          = 0,
    )


    DeclActor(
        TriggerX            = 5350,
        TriggerZ            = 50,
        TriggerY            = 109980,
        TriggerRange        = 1000,
        ActorX              = 1170,
        ActorZ              = -2060,
        ActorY              = 108860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_2D7",          # 01, 1
        "Function_2_2E2",          # 02, 2
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    Return()

    # Function_0_2D6 end

    def Function_1_2D7(): pass

    label("Function_1_2D7")

    OP_71(0x0, 0x4)
    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_2D7 end

    def Function_2_2E2(): pass

    label("Function_2_2E2")

    EventBegin(0x1)

    ChrTalk(    #0
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_30E():
        OP_6D(3000, 20, 108970, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_30E)

    def lambda_326():
        OP_67(0, 8000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_326)

    def lambda_33E():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_33E)

    def lambda_34E():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_34E)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D5")
    OP_C0(0xE, 0x20, 0x14E6, 0x32, 0x1AD9C, 0x10E, 0x78A, 0xFFFFFC18, 0x1A928)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_3E4")

    label("loc_3D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E4")
    EventEnd(0x1)

    label("loc_3E4")

    Return()

    # Function_2_2E2 end

    SaveToFile()

Try(main)
