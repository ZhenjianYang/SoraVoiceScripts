from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0602   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0602.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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


    DeclActor(
        TriggerX            = -1160,
        TriggerZ            = 0,
        TriggerY            = 144370,
        TriggerRange        = 1700,
        ActorX              = -1160,
        ActorZ              = 2500,
        ActorY              = 144370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13210,
        TriggerZ            = 0,
        TriggerY            = 169110,
        TriggerRange        = 1700,
        ActorX              = -13210,
        ActorZ              = 2500,
        ActorY              = 169110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4340,
        TriggerZ            = 0,
        TriggerY            = 181980,
        TriggerRange        = 1700,
        ActorX              = 4340,
        ActorZ              = 2500,
        ActorY              = 181980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30880,
        TriggerZ            = 0,
        TriggerY            = 150510,
        TriggerRange        = 1700,
        ActorX              = -30880,
        ActorZ              = 2500,
        ActorY              = 150510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_201",          # 02, 2
        "Function_3_393",          # 03, 3
        "Function_4_525",          # 04, 4
        "Function_5_6B7",          # 05, 5
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Return()

    # Function_0_13A end

    def Function_1_13B(): pass

    label("Function_1_13B")

    OP_72(0x0, 0x28)
    OP_72(0x1, 0x28)
    OP_72(0x2, 0x28)
    OP_72(0x3, 0x28)
    OP_72(0x4, 0x28)
    OP_72(0x5, 0x28)
    OP_72(0x6, 0x28)
    OP_72(0x7, 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_178")
    OP_6F(0x1, 120)
    OP_6F(0x6, 60)

    label("loc_178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18D")
    OP_6F(0x1, 120)
    OP_6F(0x6, 160)

    label("loc_18D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1A2")
    OP_6F(0x3, 120)
    OP_6F(0x2, 60)

    label("loc_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B7")
    OP_6F(0x3, 120)
    OP_6F(0x2, 160)

    label("loc_1B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1CC")
    OP_6F(0x4, 120)
    OP_6F(0x5, 60)

    label("loc_1CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1E1")
    OP_6F(0x4, 120)
    OP_6F(0x5, 160)

    label("loc_1E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1F6")
    OP_6F(0x7, 60)
    OP_6F(0x0, 260)

    label("loc_1F6")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_13B end

    def Function_2_201(): pass

    label("Function_2_201")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)

    AnonymousTalk(    #0
        "There is a lever. Move it?\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E3")

    Menu(
        0,
        260,
        200,
        0,
        (
            "Drop To The Right\x01",      # 0
            "Drop To The Left\x01",       # 1
            "Don't Move\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296")
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3C)
    OP_73(0x6)
    OP_A2(0x1)
    Jump("loc_2B7")

    label("loc_296")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B7")
    OP_6F(0x6, 100)
    OP_70(0x6, 0xA0)
    OP_73(0x6)
    OP_A2(0x0)

    label("loc_2B7")

    OP_6D(3880, 0, 135860, 500)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_73(0x1)
    OP_69(0x0, 0x258)
    Jump("loc_38A")

    label("loc_2E3")


    Menu(
        0,
        260,
        200,
        0,
        (
            "Return To Original Position\x01",      # 0
            "Don't Move\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_346")
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_73(0x6)
    OP_A3(0x1)
    Jump("loc_361")

    label("loc_346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_361")
    OP_6F(0x6, 160)
    OP_70(0x6, 0x64)
    OP_73(0x6)
    OP_A3(0x0)

    label("loc_361")

    OP_6D(3880, 0, 135860, 500)
    OP_6F(0x1, 120)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_69(0x0, 0x258)

    label("loc_38A")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_2_201 end

    def Function_3_393(): pass

    label("Function_3_393")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)

    AnonymousTalk(    #1
        "There is a lever. Move it?\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_475")

    Menu(
        0,
        260,
        200,
        0,
        (
            "Drop To The Right\x01",      # 0
            "Drop To The Left\x01",       # 1
            "Don't Move\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    OP_73(0x2)
    OP_A2(0x3)
    Jump("loc_449")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449")
    OP_6F(0x2, 100)
    OP_70(0x2, 0xA0)
    OP_73(0x2)
    OP_A2(0x2)

    label("loc_449")

    OP_6D(-12270, 0, 174500, 500)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    OP_73(0x3)
    OP_69(0x0, 0x258)
    Jump("loc_51C")

    label("loc_475")


    Menu(
        0,
        260,
        200,
        0,
        (
            "Return To Original Position\x01",      # 0
            "Don't Move\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4D8")
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    OP_A3(0x3)
    Jump("loc_4F3")

    label("loc_4D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4F3")
    OP_6F(0x2, 160)
    OP_70(0x2, 0x64)
    OP_73(0x2)
    OP_A3(0x2)

    label("loc_4F3")

    OP_6D(-12270, 0, 174500, 500)
    OP_6F(0x3, 120)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_69(0x0, 0x258)

    label("loc_51C")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_3_393 end

    def Function_4_525(): pass

    label("Function_4_525")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)

    AnonymousTalk(    #2
        "There is a lever. Move it?\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_607")

    Menu(
        0,
        260,
        200,
        0,
        (
            "Drop To The Right\x01",      # 0
            "Drop To The Left\x01",       # 1
            "Don't Move\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA")
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3C)
    OP_73(0x5)
    OP_A2(0x5)
    Jump("loc_5DB")

    label("loc_5BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DB")
    OP_6F(0x5, 100)
    OP_70(0x5, 0xA0)
    OP_73(0x5)
    OP_A2(0x4)

    label("loc_5DB")

    OP_6D(-8090, -60, 183030, 500)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x78)
    OP_73(0x4)
    OP_69(0x0, 0x258)
    Jump("loc_6AE")

    label("loc_607")


    Menu(
        0,
        260,
        200,
        0,
        (
            "Return To Original Position\x01",      # 0
            "Don't Move\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_66A")
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    OP_A3(0x5)
    Jump("loc_685")

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_685")
    OP_6F(0x5, 160)
    OP_70(0x5, 0x64)
    OP_73(0x5)
    OP_A3(0x4)

    label("loc_685")

    OP_6D(-8090, -60, 183030, 500)
    OP_6F(0x4, 120)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_69(0x0, 0x258)

    label("loc_6AE")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_4_525 end

    def Function_5_6B7(): pass

    label("Function_5_6B7")

    SetMapFlags(0x80)
    ClearMapFlags(0x1)

    AnonymousTalk(    #3
        "There is a lever. Move it?\x02",
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_739")

    Menu(
        0,
        260,
        200,
        0,
        (
            "Drop\x01",            # 0
            "Don't Move\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    EventBegin(0x0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x3C)
    OP_73(0x7)
    OP_6F(0x0, 0)
    OP_70(0x0, 0xFA)
    OP_73(0x0)
    OP_A2(0x6)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    label("loc_739")


    Menu(
        0,
        260,
        200,
        0,
        (
            "Raise\x01",           # 0
            "Don't Move\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    EventBegin(0x0)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)
    OP_73(0x7)
    OP_6F(0x0, 250)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_A3(0x6)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    # Function_5_6B7 end

    SaveToFile()

Try(main)
