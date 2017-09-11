from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'R4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'R4100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60020",
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
        'Kloe',                                 # 9
        '1st Lieutenant Schwarz',               # 10
        'Sieg',                                 # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Military K-9',                         # 15
        'Military K-9',                         # 16
        'Military K-9',                         # 17
        'Military K-9',                         # 18
        'Military K-9',                         # 19
        'Soldier',                              # 20
        'Soldier',                              # 21
        'Soldier',                              # 22
        'Soldier',                              # 23
        'Soldier',                              # 24
        'Sanktheim Gate',                       # 25
        'Erbe Scenic Route',                    # 26
        'Grancel City',                         # 27
        'フレイムプラント',                     # 28
        'フレイムプラント',                     # 29
        'ヘルマーズ',                           # 30
        'ヘルマーズ',                           # 31
        '沼チュパカブラ',                       # 32
        '沼チュパカブラ',                       # 33
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
        'ED6_DT07/CH00040 ._CH',             # 00
        'ED6_DT06/CH20114 ._CH',             # 01
        'ED6_DT07/CH02320 ._CH',             # 02
        'ED6_DT07/CH00341 ._CH',             # 03
        'ED6_DT09/CH10061 ._CH',             # 04
        'ED6_DT07/CH01640 ._CH',             # 05
        'ED6_DT06/CH20115 ._CH',             # 06
        'ED6_DT07/CH00041 ._CH',             # 07
        'ED6_DT09/CH10060 ._CH',             # 08
        'ED6_DT09/CH10780 ._CH',             # 09
        'ED6_DT09/CH10781 ._CH',             # 0A
        'ED6_DT09/CH10790 ._CH',             # 0B
        'ED6_DT09/CH10791 ._CH',             # 0C
        'ED6_DT09/CH10050 ._CH',             # 0D
        'ED6_DT09/CH10051 ._CH',             # 0E
        'ED6_DT09/CH10800 ._CH',             # 0F
        'ED6_DT09/CH10801 ._CH',             # 10
        'ED6_DT09/CH10810 ._CH',             # 11
        'ED6_DT09/CH10811 ._CH',             # 12
        'ED6_DT09/CH10820 ._CH',             # 13
        'ED6_DT09/CH10821 ._CH',             # 14
        'ED6_DT09/CH11220 ._CH',             # 15
        'ED6_DT09/CH11221 ._CH',             # 16
        'ED6_DT09/CH11230 ._CH',             # 17
        'ED6_DT09/CH11231 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH00040P._CP',             # 00
        'ED6_DT06/CH20114P._CP',             # 01
        'ED6_DT07/CH02320P._CP',             # 02
        'ED6_DT07/CH00341P._CP',             # 03
        'ED6_DT09/CH10061P._CP',             # 04
        'ED6_DT07/CH01640P._CP',             # 05
        'ED6_DT06/CH20115P._CP',             # 06
        'ED6_DT07/CH00041P._CP',             # 07
        'ED6_DT09/CH10060P._CP',             # 08
        'ED6_DT09/CH10780P._CP',             # 09
        'ED6_DT09/CH10781P._CP',             # 0A
        'ED6_DT09/CH10790P._CP',             # 0B
        'ED6_DT09/CH10791P._CP',             # 0C
        'ED6_DT09/CH10050P._CP',             # 0D
        'ED6_DT09/CH10051P._CP',             # 0E
        'ED6_DT09/CH10800P._CP',             # 0F
        'ED6_DT09/CH10801P._CP',             # 10
        'ED6_DT09/CH10810P._CP',             # 11
        'ED6_DT09/CH10811P._CP',             # 12
        'ED6_DT09/CH10820P._CP',             # 13
        'ED6_DT09/CH10821P._CP',             # 14
        'ED6_DT09/CH11220P._CP',             # 15
        'ED6_DT09/CH11221P._CP',             # 16
        'ED6_DT09/CH11230P._CP',             # 17
        'ED6_DT09/CH11231P._CP',             # 18
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -41770,
        Z                   = 0,
        Y                   = -5530,
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
        X                   = 137370,
        Z                   = -2050,
        Y                   = 5100,
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
        X                   = -16930,
        Z                   = 0,
        Y                   = 111160,
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
        X                   = 13640,
        Z                   = -40,
        Y                   = -2250,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16650,
        Z                   = 300,
        Y                   = 2360,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15450,
        Z                   = -30,
        Y                   = 56010,
        Unknown_0C          = 0,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13350,
        Z                   = 110,
        Y                   = 68880,
        Unknown_0C          = 0,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 60840,
        Z                   = 10,
        Y                   = 16239,
        Unknown_0C          = 0,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 105890,
        Z                   = -1980,
        Y                   = 18620,
        Unknown_0C          = 0,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 16690,
        Y                   = -1000,
        Z                   = 31700,
        Range               = 36480,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5546,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 31170,
        TriggerZ            = 0,
        TriggerY            = 32450,
        TriggerRange        = 1500,
        ActorX              = 31170,
        ActorZ              = 1700,
        ActorY              = 32450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29270,
        TriggerZ            = 0,
        TriggerY            = 21060,
        TriggerRange        = 1500,
        ActorX              = 29270,
        ActorZ              = 1800,
        ActorY              = 21060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34440,
        TriggerZ            = 0,
        TriggerY            = 31310,
        TriggerRange        = 1500,
        ActorX              = 34440,
        ActorZ              = 1700,
        ActorY              = 31310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_506",          # 00, 0
        "Function_1_534",          # 01, 1
        "Function_2_547",          # 02, 2
        "Function_3_1317",         # 03, 3
        "Function_4_1E2F",         # 04, 4
        "Function_5_1E5D",         # 05, 5
        "Function_6_1E8B",         # 06, 6
        "Function_7_1EB9",         # 07, 7
        "Function_8_1F10",         # 08, 8
        "Function_9_1F58",         # 09, 9
    )


    def Function_0_506(): pass

    label("Function_0_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_522")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_522")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_506 end

    def Function_1_534(): pass

    label("Function_1_534")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE90D0, 0x3003B)
    Return()

    # Function_1_534 end

    def Function_2_547(): pass

    label("Function_2_547")

    ClearMapFlags(0x10000000)
    OP_B6(0x0)
    EventBegin(0x0)
    OP_6D(94030, -2000, 13780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0x9, 103460, -2000, 12700, 270)
    SetChrPos(0x8, 104570, -2000, 10950, 270)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 96990, 7000, 16000, 90)
    OP_8E(0x9, 0x172B4, 0xFFFFF830, 0x3598, 0x1388, 0x0)
    SetChrChipByIndex(0x9, 6)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)
    OP_8C(0x9, 135, 800)

    ChrTalk(    #0
        0x9,
        "#172F#6PKloe! This way!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 7)

    def lambda_63B():
        OP_8E(0xFE, 0x14C44, 0x28, 0x337C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_63B)
    Sleep(1000)
    OP_8C(0x9, 270, 800)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 1)

    def lambda_66C():
        OP_8E(0xFE, 0x1482A, 0x50, 0x35FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_66C)

    def lambda_687():
        OP_6C(57000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_687)

    def lambda_697():
        OP_6D(84370, 60, 13300, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_697)
    WaitChrThread(0x9, 0x1)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 6)
    SetChrFlags(0x9, 0x20)
    TurnDirection(0x9, 0x8, 800)

    def lambda_6D0():

        label("loc_6D0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_6D0")

    QueueWorkItem2(0x9, 1, lambda_6D0)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 0)

    ChrTalk(    #1
        0x8,
        (
            "#043F#4P*huff* *huff*... We're finally\x01",
            "off the Erbe Scenic Route.\x02\x03",

            "What should we do now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#170FPlease, exit onto the Royal Avenue\x01",
            "from here, and head to Grancel.\x02\x03",

            "My men are causing enough of a\x01",
            "diversion that security should\x01",
            "be stretched pretty thinly.\x02\x03",

            "If everything looks okay, you keep\x01",
            "on to the Bracer Guild...without\x01",
            "getting spotted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#042F#4PI understand...oh.\x02\x03",

            "But what about you...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#170FI'll hold the enemy off here.\x02\x03",

            "I should be able to buy you\x01",
            "a little extra time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#043F#4PNo... No, you can't!\x02\x03",

            "I can't go on my own...\x02\x03",

            "I'll fight at your side!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "#176FWe all have something to protect...\x02\x03",

            "I will stay here, for my convictions\x01",
            "and my duty...\x02\x03",

            "#170F...and most importantly for you, my\x01",
            "lady. Forgive my impertinence, but you\x01",
            "are of paramount importance to me.\x02\x03",

            "I will guard you with my life,\x01",
            "and I ask only that you remember\x01",
            "me as your friend and confidant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#049F#4P...\x02\x03",

            "#047FI understand, Julia.\x02\x03",

            "#040FBut please, promise... Promise me\x01",
            "you won't do anything reckless...\x02\x03",

            "...and that we will meet again in\x01",
            "better circumstances and take tea\x01",
            "with my grandmother.\x02\x03",

            "#041FI'll bake for you... I'll try a\x01",
            "new recipe, and bake you something\x01",
            "sweet and delicious!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "#171FI look forward to it.\x02\x03",

            "Now, please hurry.\x02\x03",

            "#172FSieg! Look after her for me!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BEE():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BEE)
    OP_22(0x197, 0x0, 0x64)

    def lambda_C01():

        label("loc_C01")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_C01")

    QueueWorkItem2(0x8, 1, lambda_C01)
    SetChrFlags(0xA, 0x1)

    def lambda_C17():
        OP_8E(0xFE, 0x14492, 0xFA0, 0x3F8E, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C17)
    Sleep(200)
    OP_8C(0x8, 270, 300)
    SetChrChipByIndex(0x8, 7)

    def lambda_C43():
        OP_8E(0xFE, 0x10A18, 0x0, 0x337C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C43)

    def lambda_C5E():

        label("loc_C5E")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_C5E")

    QueueWorkItem2(0x9, 1, lambda_C5E)
    Sleep(100)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_C79():
        OP_6D(82000, 0, 13970, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C79)
    WaitChrThread(0xA, 0x1)
    OP_8E(0xA, 0xFB72, 0x7D0, 0x3F8E, 0x2328, 0x0)
    OP_44(0x9, 0xFF)
    SetChrPos(0xE, 108880, -2000, 5290, 0)
    SetChrPos(0xF, 110190, -2000, 6430, 0)
    SetChrPos(0x10, 111910, -2000, 6760, 0)
    SetChrPos(0x11, 109570, -2000, 3930, 0)
    SetChrPos(0x12, 110140, -2000, 2710, 0)
    SetChrPos(0xB, 111470, -2000, 4930, 0)
    SetChrPos(0xC, 112960, -2000, 5790, 0)
    SetChrPos(0xD, 112000, -2000, 3870, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #9
        0x9,
        (
            "#176FWell, now...\x01",
            "They've finally caught up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    def lambda_D9C():
        OP_6C(314000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D9C)

    def lambda_DAC():
        OP_6D(100950, -2000, 14190, 2900)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DAC)
    Sleep(2000)

    def lambda_DC9():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DC9)

    def lambda_DE4():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DE4)

    def lambda_DFF():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_DFF)

    def lambda_E1A():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E1A)

    def lambda_E35():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E35)

    def lambda_E50():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E50)

    def lambda_E6B():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E6B)

    def lambda_E86():
        OP_90(0xFE, 0xFFFFE0C0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E86)
    Sleep(900)
    SetChrPos(0x9, 80010, 80, 13820, 0)
    TurnDirection(0x9, 0xB, 0)

    def lambda_EBE():
        OP_67(0, 6770, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_EBE)

    def lambda_ED6():
        OP_6B(3920, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_ED6)

    def lambda_EE6():
        OP_6D(88700, 0, 13370, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EE6)
    Sleep(1000)

    def lambda_F03():
        OP_90(0xFE, 0xFFFFD508, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F03)

    def lambda_F1E():
        OP_90(0xFE, 0xFFFFD508, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_F1E)
    Sleep(100)

    def lambda_F3E():
        OP_90(0xFE, 0xFFFFD508, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F3E)

    def lambda_F59():
        OP_90(0xFE, 0xFFFFD508, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F59)
    Sleep(100)

    def lambda_F79():
        OP_90(0xFE, 0xFFFFD6FC, 0x0, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F79)
    Sleep(200)

    def lambda_F99():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F99)
    Sleep(100)

    def lambda_FB9():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_FB9)
    Sleep(100)

    def lambda_FD9():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFFD44, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FD9)
    WaitChrThread(0xE, 0x1)
    SetChrChipByIndex(0xE, 8)
    SetChrChipByIndex(0xF, 8)

    def lambda_1003():

        label("loc_1003")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1003")

    QueueWorkItem2(0xE, 0, lambda_1003)

    def lambda_1016():

        label("loc_1016")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1016")

    QueueWorkItem2(0xF, 0, lambda_1016)
    WaitChrThread(0x10, 0x1)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x11, 8)

    def lambda_1038():

        label("loc_1038")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1038")

    QueueWorkItem2(0x10, 0, lambda_1038)

    def lambda_104B():

        label("loc_104B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_104B")

    QueueWorkItem2(0x11, 0, lambda_104B)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 8)

    def lambda_1068():

        label("loc_1068")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1068")

    QueueWorkItem2(0x12, 0, lambda_1068)
    WaitChrThread(0xD, 0x1)

    ChrTalk(    #10
        0x9,
        (
            "#170FThree men...and five dogs.\x02\x03",

            "#176FHeh...\x01",
            "I think you underestimate me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10D0():
        OP_6D(80740, 0, 14730, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10D0)
    OP_6B(3200, 1200)

    ChrTalk(    #11
        0x9,
        (
            "#176FAs he taught me how to wield a\x01",
            "blade...the time to truly use\x01",
            "it has come.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x1F8, 0x0, 0x64)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(800)

    ChrTalk(    #12
        0x9,
        (
            "#172FI, Julia Schwarz...commander\x01",
            "of the Royal Guardsmen...\x02\x03",

            "#177F...will not yield!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 1)

    def lambda_11CD():
        OP_6D(88700, 0, 13370, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11CD)

    def lambda_11E5():
        OP_8E(0xFE, 0x15E3C, 0xFFFFFC18, 0x3732, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11E5)
    Sleep(200)
    SetChrChipByIndex(0xE, 4)

    def lambda_120A():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_120A)
    Sleep(50)
    SetChrChipByIndex(0xF, 4)
    SetChrChipByIndex(0x10, 4)

    def lambda_1234():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1234)

    def lambda_124F():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_124F)
    Sleep(100)
    SetChrChipByIndex(0x11, 4)

    def lambda_1274():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1274)
    Sleep(50)
    SetChrChipByIndex(0x12, 4)

    def lambda_1299():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1299)

    def lambda_12B4():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12B4)
    Sleep(100)

    def lambda_12D4():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12D4)

    def lambda_12EF():
        OP_8E(0xFE, 0x1291C, 0x0, 0x3642, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12EF)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/R4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_547 end

    def Function_3_1317(): pass

    label("Function_3_1317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E2E")
    OP_A2(0x607)
    EventBegin(0x0)
    SetChrPos(0x13, 23950, 0, 33710, 180)
    SetChrPos(0x14, 22810, 0, 34790, 180)
    SetChrPos(0x15, 25010, 0, 34710, 180)
    SetChrPos(0x16, 23120, 0, 36550, 180)
    SetChrPos(0x17, 24610, 0, 36760, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    ChrTalk(    #13
        0x13,
        "Hey! You there!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 0)
    TurnDirection(0x102, 0x13, 0)
    TurnDirection(0x10E, 0x13, 0)

    def lambda_13C6():
        OP_8E(0xFE, 0x63A6, 0x0, 0x78C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_13C6)

    def lambda_13E1():
        OP_8E(0xFE, 0x5EBA, 0x0, 0x7BAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_13E1)

    def lambda_13FC():
        OP_8E(0xFE, 0x5E06, 0x0, 0x82BE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_13FC)

    def lambda_1417():
        OP_8E(0xFE, 0x669E, 0x0, 0x7EFD, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1417)

    def lambda_1432():
        OP_8E(0xFE, 0x64C8, 0x0, 0x8426, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1432)

    def lambda_144D():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_144D)
    OP_6D(23860, 0, 33760, 2000)
    SetChrPos(0x101, 25010, 0, 20590, 0)
    SetChrPos(0x102, 23710, 0, 20590, 0)
    SetChrPos(0x10E, 23720, 0, 19280, 0)

    def lambda_14A1():

        label("loc_14A1")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14A1")

    QueueWorkItem2(0x13, 1, lambda_14A1)

    def lambda_14B2():

        label("loc_14B2")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14B2")

    QueueWorkItem2(0x14, 1, lambda_14B2)

    def lambda_14C3():

        label("loc_14C3")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14C3")

    QueueWorkItem2(0x15, 1, lambda_14C3)

    def lambda_14D4():

        label("loc_14D4")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14D4")

    QueueWorkItem2(0x16, 1, lambda_14D4)

    def lambda_14E5():

        label("loc_14E5")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_14E5")

    QueueWorkItem2(0x17, 1, lambda_14E5)

    def lambda_14F6():
        OP_6D(25030, 0, 29550, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14F6)

    def lambda_150E():
        OP_8E(0xFE, 0x6626, 0x0, 0x6D88, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_150E)

    def lambda_1529():
        OP_8E(0xFE, 0x613A, 0x0, 0x6CFC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1529)

    def lambda_1544():
        OP_8E(0xFE, 0x631A, 0x0, 0x6838, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1544)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #14
        0x101,
        "#004F(Huh...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        "#012F(Looks like an army unit...)\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x2)

    ChrTalk(    #16
        0x13,
        (
            "No tourists are allowed at the\x01",
            "Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x2)

    ChrTalk(    #17
        0x13,
        (
            "Did you not see the ordinance\x01",
            "that was just posted all over\x01",
            "the city streets?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#505F???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#010FActually...we're not citizens\x01",
            "of Grancel.\x02\x03",

            "We just recently came here, by\x01",
            "way of the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x15,
        "Travelers, eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x14,
        (
            "Hard to believe anyone would want\x01",
            "to walk on the highways with\x01",
            "terrorist activity going on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x14,
        "Talk about reckless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#004FUmm...setting aside the terrorist\x01",
            "discussion for a second...\x02\x03",

            "What's the 'Erbe Royal Villa'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10E,
        (
            "#130FIt's a small palace to the east,\x01",
            "where the royal family resides.\x02\x03",

            "I was given to understand that\x01",
            "the townsfolk often went there\x01",
            "to relax...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x13,
        "#4PSorry, but it's off-limits for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x13,
        (
            "The army's using it as a base of\x01",
            "operations for investigating the\x01",
            "terrorist activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#012FYou don't say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x13,
        "The roads nearby aren't off-limits...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x13,
        (
            "...but I'd suggest you keep away,\x01",
            "just to make sure no one mistakes\x01",
            "you for one of the bad guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x13, 0x63EC, 0x0, 0x75E4, 0xBB8, 0x0)

    def lambda_198A():
        OP_8F(0xFE, 0x5BAE, 0xFFFFFFF6, 0x7080, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_198A)

    def lambda_19A5():
        OP_8F(0xFE, 0x5C1C, 0xFFFFFFF6, 0x6CAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19A5)

    def lambda_19C0():
        OP_8F(0xFE, 0x5BD6, 0xFFFFFFF6, 0x6702, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 2, lambda_19C0)

    def lambda_19DB():

        label("loc_19DB")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_19DB")

    QueueWorkItem2(0x101, 1, lambda_19DB)

    def lambda_19EC():

        label("loc_19EC")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_19EC")

    QueueWorkItem2(0x102, 1, lambda_19EC)

    def lambda_19FD():

        label("loc_19FD")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_19FD")

    QueueWorkItem2(0x10E, 1, lambda_19FD)
    OP_43(0x13, 0x1, 0x0, 0x4)
    OP_43(0x16, 0x1, 0x0, 0x5)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x6)
    OP_43(0x14, 0x1, 0x0, 0x5)
    Sleep(150)
    OP_43(0x17, 0x1, 0x0, 0x6)
    Sleep(1000)
    OP_6D(23230, -10, 27690, 3000)
    WaitChrThread(0x17, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10E, 0xFF)

    ChrTalk(    #30
        0x10E,
        (
            "#130FWell, that's certainly grim.\x02\x03",

            "Personally, being told not to go\x01",
            "somewhere just makes me want to go\x01",
            "and see what all the fuss is about.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(    #31
        0x10E,
        (
            "#130FWhat do you say? Want to go poke\x01",
            "around and see what we can see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#007FUmm...\x01",
            "It's not that I'm not curious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#015FWe did just get that warning, so\x01",
            "I think it's best to hold off.\x02\x03",

            "There may actually be terrorists,\x01",
            "like the soldiers said.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #34
        0x101,
        (
            "#505FWell...\x02\x03",

            "I think the Intelligence Division\x01",
            "is just using the Royal Guardsmen\x01",
            "and bracers as scapegoats...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #35
        0x102,
        "#012FEstelle!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #36
        0x102,
        (
            "#013F(You really need to not say\x01",
            "things like that out loud.)\x02\x03",

            "(If someone overhears you, then\x01",
            "we're apt to get caught up in it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#002F(Y-Yeah, you're right...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x102, 400)

    ChrTalk(    #38
        0x10E,
        (
            "#131F???\x02\x03",

            "Intelligence what now?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x10E, 400)

    ChrTalk(    #39
        0x101,
        (
            "#506FUmm, err, let's see...\x02\x03",

            "Sorry. It's nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        "#010FAnyway, let's head on to the city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10E,
        (
            "#130F*sigh*...\x01",
            "Oh, all right. You kids are no fun.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_1E2E")

    Return()

    # Function_3_1317 end

    def Function_4_1E2F(): pass

    label("Function_4_1E2F")

    OP_8E(0xFE, 0x6586, 0x0, 0x611C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x55F0, 0x0, 0x41AA, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_1E2F end

    def Function_5_1E5D(): pass

    label("Function_5_1E5D")

    OP_8E(0xFE, 0x60E0, 0x0, 0x6554, 0xBB8, 0x0)
    OP_8E(0xFE, 0x52BC, 0x0, 0x461E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_1E5D end

    def Function_6_1E8B(): pass

    label("Function_6_1E8B")

    OP_8E(0xFE, 0x67D4, 0x0, 0x5EA6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x5C08, 0x0, 0x4646, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_1E8B end

    def Function_7_1EB9(): pass

    label("Function_7_1EB9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        "\x07\x05North: Grancel             179 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_1EB9 end

    def Function_8_1F10(): pass

    label("Function_8_1F10")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #43
        "\x07\x05South: Sanktheim Gate\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1F10 end

    def Function_9_1F58(): pass

    label("Function_9_1F58")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #44
        "\x07\x05East:  Erbe Royal Villa    224 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_1F58 end

    SaveToFile()

Try(main)
