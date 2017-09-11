from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4213   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4213.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Special Ops Soldier',                  # 9
        'Special Ops Soldier',                  # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        '1st Lieutenant Schwarz',               # 14
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH01330 ._CH',             # 03
        'ED6_DT07/CH00340 ._CH',             # 04
        'ED6_DT06/CH20042 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00111 ._CH',             # 07
        'ED6_DT07/CH00170 ._CH',             # 08
        'ED6_DT07/CH00171 ._CH',             # 09
        'ED6_DT07/CH00130 ._CH',             # 0A
        'ED6_DT07/CH00131 ._CH',             # 0B
        'ED6_DT07/CH02090 ._CH',             # 0C
        'ED6_DT07/CH00440 ._CH',             # 0D
        'ED6_DT07/CH00441 ._CH',             # 0E
        'ED6_DT06/CH20039 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH01330P._CP',             # 03
        'ED6_DT07/CH00340P._CP',             # 04
        'ED6_DT06/CH20042P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00111P._CP',             # 07
        'ED6_DT07/CH00170P._CP',             # 08
        'ED6_DT07/CH00171P._CP',             # 09
        'ED6_DT07/CH00130P._CP',             # 0A
        'ED6_DT07/CH00131P._CP',             # 0B
        'ED6_DT07/CH02090P._CP',             # 0C
        'ED6_DT07/CH00440P._CP',             # 0D
        'ED6_DT07/CH00441P._CP',             # 0E
        'ED6_DT06/CH20039P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_296",          # 01, 1
        "Function_2_2B5",          # 02, 2
        "Function_3_2CB",          # 03, 3
        "Function_4_41F",          # 04, 4
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_214")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_214")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_220"),
        (SWITCH_DEFAULT, "loc_23F"),
    )


    label("loc_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x661)
    Event(0, 4)

    label("loc_23C")

    Jump("loc_23F")

    label("loc_23F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_266")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 74910, 0, -38410, 99)
    OP_43(0xD, 0x0, 0x0, 0x2)
    Jump("loc_295")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_270")
    Jump("loc_295")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_27A")
    Jump("loc_295")

    label("loc_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_284")
    Jump("loc_295")

    label("loc_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_28E")
    Jump("loc_295")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_295")

    label("loc_295")

    Return()

    # Function_0_1EA end

    def Function_1_296(): pass

    label("Function_1_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AB")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_296 end

    def Function_2_2B5(): pass

    label("Function_2_2B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2B5")

    label("loc_2CA")

    Return()

    # Function_2_2B5 end

    def Function_3_2CB(): pass

    label("Function_3_2CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_365")

    ChrTalk(    #0
        0x112,
        (
            "#170FNow I understand just how\x01",
            "inexperienced I really am.\x02\x03",

            "I've been training, just so I\x01",
            "wouldn't embarrass myself when\x01",
            "they came back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41B")

    label("loc_365")

    OP_A2(0x0)

    ChrTalk(    #1
        0x112,
        (
            "#170FWhew...\x01",
            "Finally made it back here...\x02\x03",

            "Now I understand just how\x01",
            "inexperienced I really am.\x02\x03",

            "I've been training, just so I\x01",
            "wouldn't embarrass myself when\x01",
            "they came back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41B")

    TalkEnd(0xFE)
    Return()

    # Function_3_2CB end

    def Function_4_41F(): pass

    label("Function_4_41F")

    EventBegin(0x0)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x108, 8)
    SetChrChipByIndex(0x104, 10)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x102, 66560, 0, -30890, 186)
    SetChrPos(0x108, 65640, 0, -29760, 182)
    SetChrPos(0x104, 67130, 0, -29550, 172)
    SetChrPos(0x8, 68760, 0, -39520, 135)
    SetChrPos(0x9, 69890, 0, -40660, 315)
    SetChrPos(0xB, 65730, 0, -41730, 270)
    SetChrPos(0xC, 64099, 0, -41250, 90)
    OP_6D(68190, 0, -42370, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6D(67700, 0, -42570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6F(0x0, 60)
    OP_72(0x0, 0x10)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_59E():
        OP_6D(66270, 0, -37030, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_59E)

    def lambda_5B6():
        OP_6E(300, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5B6)

    def lambda_5C6():
        OP_67(0, 5550, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5C6)

    def lambda_5DE():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5DE)
    Sleep(100)

    def lambda_5F1():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5F1)
    Sleep(100)

    def lambda_604():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_604)
    Sleep(100)

    def lambda_617():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_617)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #2
        0x8,
        "#2PWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        "#2PIntruders?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x104,
        (
            "#031F#6PWell, yes, I guess you could\x01",
            "call us that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x108,
        "#070F#6PI guess I can understand the sentiment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#016F#6PLet's go!\x02",
    )

    CloseMessageWindow()

    def lambda_6D2():
        OP_8E(0xFE, 0x10252, 0x0, 0xFFFF33AA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6D2)

    def lambda_6ED():
        OP_8E(0xFE, 0x10252, 0x0, 0xFFFF33AA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_6ED)
    Sleep(50)

    def lambda_70D():
        OP_8E(0xFE, 0x10252, 0x0, 0xFFFF33AA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_70D)

    def lambda_728():
        OP_6D(65930, 0, -40190, 800)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_728)

    def lambda_740():
        OP_6E(225, 800)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_740)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x8, 4)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0xB, 4)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x9, 13)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0xC, 13)
    Sleep(350)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x104, 0xFF)
    Battle(0x3A9, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_7DF"),
        (SWITCH_DEFAULT, "loc_7E2"),
    )


    label("loc_7DF")

    OP_B4(0x0)
    Return()

    label("loc_7E2")

    EventBegin(0x0)
    OP_6D(69880, 0, -41130, 0)
    OP_6E(309, 0)
    SetChrPos(0x102, 70860, 0, -41870, 270)
    SetChrPos(0x104, 70610, 0, -40330, 225)
    SetChrPos(0x108, 69080, 0, -40260, 180)
    SetChrPos(0x8, 68030, 0, -44480, 135)
    SetChrPos(0x9, 68470, 0, -46180, 107)
    SetChrPos(0xB, 67960, 0, -42620, 270)
    SetChrPos(0xC, 66830, 0, -45880, 180)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0x9, 5)
    SetChrChipByIndex(0xC, 5)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x104, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x108, 8)
    SetChrChipByIndex(0x104, 10)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #7
        0x108,
        "#070FThat takes care of them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x104,
        "#035FNighty-night, kitty-cats...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)
    OP_8C(0x102, 90, 600)
    SetChrFlags(0x102, 0x4)

    def lambda_986():
        OP_8E(0xFE, 0x120F2, 0x0, 0xFFFF5B5A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_986)
    SetChrChipByIndex(0x104, 65535)
    SetChrChipByIndex(0x108, 65535)

    def lambda_9AB():

        label("loc_9AB")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_9AB")

    QueueWorkItem2(0x108, 1, lambda_9AB)

    def lambda_9BC():

        label("loc_9BC")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_9BC")

    QueueWorkItem2(0x104, 1, lambda_9BC)
    OP_6D(72350, 0, -40970, 1500)
    WaitChrThread(0x102, 0x1)
    OP_44(0x108, 0xFF)
    OP_44(0x104, 0xFF)

    ChrTalk(    #9
        0x102,
        (
            "#016FLet's see what we can do about\x01",
            "this gate control...\x02\x03",

            "Keep your eyes open for any\x01",
            "more Special Ops!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x108,
        "#076F#6PLeave it to us.\x02",
    )

    CloseMessageWindow()

    def lambda_A75():
        OP_69(0xFE, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A75)
    OP_8C(0x108, 270, 400)
    SetChrChipByIndex(0x108, 8)
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #11
        0x108,
        (
            "#077F#6PNo one's getting through here, or\x01",
            "my name isn't 'Zin the Immovable'!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 180, 400)
    SetChrFlags(0x104, 0x2)
    OP_51(0x104, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x104, 15)
    SetChrSubChip(0x104, 0)
    OP_99(0x104, 0x0, 0x3, 0x7D0)
    Sleep(300)
    OP_99(0x104, 0x3, 0xA, 0x640)
    Sleep(500)

    ChrTalk(    #12
        0x104,
        (
            "#035F#6PHeh. And now's the time that\x01",
            "Heaven's Gate opens...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x104, 0x2)
    OP_51(0x104, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x104, 0)

    def lambda_B7F():
        OP_69(0xFE, 0x320)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_B7F)
    OP_8C(0x104, 270, 400)
    SetChrChipByIndex(0x104, 10)
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #13
        0x104,
        "#030F#4PThus begins the final movement!\x02",
    )

    CloseMessageWindow()
    OP_28(0x4E, 0x4, 0x2)
    OP_28(0x4E, 0x4, 0x4)
    OP_28(0x4E, 0x1, 0x1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_41F end

    SaveToFile()

Try(main)
